from odoo import models, fields, api

class TodoList(models.Model):
                                                                                                                                                                                                                                                                                                                                                                                                  
    _description = 'To-do List'
    _order = 'id desc'

    title = fields.Char(string='Title', required=True)
    tags = fields.Many2many('todolist.tags', string='Tags', required=False)


    start_date = fields.Datetime(string='Start Date', required=True, default=fields.date.today())
    end_date = fields.Datetime(string='End Date', required=True, default=fields.date.today())

    _sql_constraints = [
        ('date_check', "CHECK ((start_date <= end_date))", "The start date must be anterior to the end date.")
    ]


    track_status = fields.Selection(
        [('draft', 'DRAFT'),
         ('in_progress', 'IN PROGRESS'),
         ('done', 'DONE')],
         default = 'draft', string="Track Status", required=True)



    ## List
    task_line_ids = fields.One2many(
        comodel_name='todolist.task.line',
        inverse_name='task_id',
        string="Task Lines")
    
    ## Invisible checkbox is_complete
    @api.onchange('track_status')
    def _onchange_track_status(self):
        # for rec in self.task_line_ids:
        #     print("---ToDoList for---")
        #     print(rec)
        #     print("------")
        #     if self.track_status == 'draft':
        #         rec.invisible_is_complete = True
        #     else:
        #         rec.invisible_is_complete = False
        
        if self.track_status == 'draft':
            self.task_line_ids.invisible_is_complete = True
        else:
            self.task_line_ids.invisible_is_complete = False



    ## Attendee
    attendee_line_ids = fields.One2many(
        comodel_name='todolist.attendee.line',
        inverse_name='task_id',
        string="Attendee Lines")
    

    ## Button Progress
    def button_in_progress(self):
        self.write({
           'track_status': "in_progress"
       })


    ## Button Done
    def button_done(self):
        self.ensure_one()
        self.write({
           'track_status': "done"
       })
        
    invisible_btn_done = fields.Boolean(string='Invisible Button Done', compute='_compute_invisible_btn_done', store=True)

    @api.depends('task_line_ids.task_is_complete', 'track_status')
    def _compute_invisible_btn_done(self):
        if self.task_line_ids:
            all_is_complete = []
            for item in self.task_line_ids:
                all_is_complete.append(item.task_is_complete)
                
            if all(all_is_complete) and self.track_status == "in_progress":
                self.invisible_btn_done = False
            else:
                self.invisible_btn_done = True

        else:
            self.invisible_btn_done = True

        # for rec in self:
        #     if rec.task_line_ids:
        #         all_is_complete = []
        #         for item in rec.task_line_ids:
        #             all_is_complete.append(item.task_is_complete)
                
        #         if all(all_is_complete) and rec.track_status == "in_progress":
        #             rec.invisible_btn_done = False
        #         else:
        #             rec.invisible_btn_done = True

        #     else:
        #         rec.invisible_btn_done = True


## List
class ToDoListLine(models.Model):
    _name = 'todolist.task.line'
    _description = 'Todo List Line'

    task_id = fields.Many2one(comodel_name= 'todolist.tasks', string='Task', ondelete='cascade')
    task_name = fields.Char(string='Name', required=True)
    task_description = fields.Text(string='Description', required=False)
    task_is_complete = fields.Boolean(string='Is Complete', required=False)
    invisible_is_complete = fields.Boolean(string='Invisible Is Complete', compute='_compute_is_complete', store=True)

    ## Invisible checkbox is_complete
    @api.depends('task_id.track_status')
    def _compute_is_complete(self):
        # for rec in self:
            
        #     if rec.task_id.track_status == 'draft':
        #         rec.invisible_is_complete = True
        #     else:
        #         rec.invisible_is_complete = False
        
        if self.task_id.track_status == 'draft':
            self.invisible_is_complete = True
        else:
            self.invisible_is_complete = False


## Attendee
class TodoListAttendeeLine(models.Model):
    _name = 'todolist.attendee.line'
    _description = 'Todo List Attendee'

    task_id = fields.Many2one(comodel_name= 'todolist.tasks', string='Task')
    attendee_name = fields.Many2one(comodel_name= 'res.users', string='Name', required=True)


## Tags
class TodoTags(models.Model):
    _name = 'todolist.tags'
    _description = 'Tags'

    name = fields.Char(string='Tags Name', required=True)
    color = fields.Integer(string='Color', required=False)