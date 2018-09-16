# WIP: CMS for AWE

## Views
- all students filter by teacher, program, class, last name, first name, day of the week, bill sent, bill payed, crud, search by name
- individual view of each student
- all staff, individual info, crud
- classroom spaces left/full -> cards for classroom with spots info, location, name etc
- changing students info only from admin panel

## Endpoints

### Login
- `/auth/token/`
- `/auth/token/verify/` 
- `/auth/token/refresh/` 
- `/auth/password-reset/`
- `/auth/password-reset/verify/`

### Students
- `/students` GET: all students 
- `/students/?first_name=Sophia` POST: search for student by *first name*, *last name*, *teacher*, *current* students, *past* students
- `/student/<int:student_id>/` POST & GET & PATCH: CRUD - admin only for create/update

### Staff
- `/staff/` GET: all staff
- `staff/<int:staff_id>/` POST & GET & PATCH: CRUD - admin only for create/update

### Classes
- `/class/` GET: all classes
- `/class/<int:class_id>/` GET: detail class info by class_id

### Sessions
- `/session/` GET: all session
- `/session/<int:session_id>/` GET: detail session info by session_id

### Classrooms
- `/classroom/` GET: all classrooms
- `/classroom/<int:classroom_id>/` GET: classroom by classroom_id
