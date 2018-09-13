# WIP: CMS for AWE

## Views
- all students filter by teacher, program, class, last name, first name, day of the week, bill sent, bill payed, crud, search by name
- individual view of each student
- all staff, individual info, crud
- classroom spaces left/full -> cards for classroom with spots info, location, name etc
- changing students info only from admin panel

## Endpoints

### Login
- `/auth/token/` done
- `/auth/token/verify/` done
- `/auth/token/refresh/` done
- `/auth/password-reset/` todo!!
- `/auth/password-reset/verify/`

### Students
- `/students` GET: all students done
- `/student/<int:student_id>/` GET: student info by student_id done
- `/students/teacher/<int:teacher_id>/` GET: all students with teacher_id
- `/students/classroom/<int:classroom_id>/` GET: all students with classroom_id
- `/students/?name=firstname` POST: search for student by first name

### Staff
- `/staff/` GET: all staff
- `staff/<int:staff_id/` GET: staff info by staff_id

### Classes
- `/class/` GET: all classes
- `/class/<int:class_id>/` GET: detail class info by class_id
- `/class/classroom/<int:classroom_id>/` GET: all classes by classroom_id

### Sessions
- `/session/` GET: all session
- `/session/<int:session_id>/` GET: detail session info by session_id
