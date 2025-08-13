from .principal_views import get_principal_data, get_principal_data_withid, create_principal_data, update_principal_data, delete_principal_data 
from .teacher_views import get_teacher_data, get_teacher_data_withid, create_teacher_data, update_teacher_data, delete_teacher_data, teacher_attendance_summary
from .students_views import get_student_data, get_student_report_card, get_student_data_withid, create_student_data, update_student_data, delete_student_data, get_students_by_section_and_grade, search_students_by_name, total_strength_by_grade
# from .fee_views import get_fee_data, reject_fee_structure, get_fee_data_withid, create_fee_data, update_fee_data, delete_fee_data, approve_structure_principal
from .fee_views import create_fee_structure, get_fee_data, reject_fee_structure, approve_structure_principal
from .fee_term_views import create_fee_term
from .fee_component_views import create_fee_component
from .course_views import create_course, list_courses
# from .course_views import get_course_data, get_course_withid, create_course_data, update_course_data, delete_course_data
from .announcement_views import get_announcement_data, get_announcement_data_withid, create_announcement_data, update_announcement_data, delete_announcement_data
from .sections_views import get_section_data, get_section_withid, create_section_data, update_section_data, delete_section_data
from .grades_views import get_grade_data, get_grade_withid, create_grade_data, update_grade_data, delete_grade_data
from .student_attendence_views import create_student_attendence_data, get_attendance_by_course_section_grade_json, get_attendance_by_course_section_grade, get_students_count_by_attendance_present, get_students_count_by_attendance_absent, get_students_count_by_attendance_leave, get_all_students_summary
from .subjects_views import get_subject_data, get_subject_withid, create_subject_data, update_subject_data, delete_subject_data
from .student_marks_views import create_student_marks_data, get_marks_by_course_section_grade, get_marks_by_subject, get_marks_by_student, get_student_marks_report
from .attachments_views import get_attachments_data
from .upload_views import create_upload_data, get_upload_data, update_upload_data
from .leave_views import get_leave_data, reject_leave, create_leave_data, farward_leave_to_principal, approve_leave_to_by_sl, approve_leave_principal
from .login_views import get_login_data, get_monthly_login_summary, get_login_withid, create_login_data, update_login_data, delete_login_data
from .fee_details_views import get_fee_details, fee_summary_view, get_fee_detail_by_id, create_fee_detail, update_fee_detail, delete_fee_detail 
from .workflow_views import start_workflow, complete_step, get_workflow_instance, get_workflow_instance_steps, get_workflow_design_for_instance, get_max_workflow_instance_id, complete_full_workflow
from .tc_views import get_tc_data, get_tc_withid, create_tc_data, update_tc_data, delete_tc_data
from .disciplinary_records_views import get_disciplinary_record_data, get_disciplinary_record_withid, create_disciplinary_record_data, update_disciplinary_record_data, delete_disciplinary_record_data
from .exam_views import get_exam_data, get_exam_withid, create_exam_data, update_exam_data, delete_exam_data
from .users_views import get_all_custom_users
from .actionrequired_views import get_action_required, manage_action_required
from .upcommingevent_views import get_upcoming_events, create_upcoming_events
from .incharge_views import get_examincharge_data, get_examincharge_withid, create_examincharge_data, update_examincharge_data, delete_examincharge_data
from .invigilator_views import get_invigilator_data, get_invigilator_withid, create_invigilator_data, update_invigilator_data, delete_invigilator_data
from .college_views import get_college_data


__all__ = ['get_principal_data', 'get_principal_data_withid', 'create_principal_data', 'update_principal_data', 'delete_principal_data', 'get_teacher_data', 
           'get_teacher_data_withid', 'create_teacher_data', 'update_teacher_data', 'delete_teacher_data', 'get_student_data', 'get_student_data_withid',
            'create_student_data', 'update_student_data', 'delete_student_data', 'get_announcement_data', 
            'get_announcement_data_withid', 'create_announcement_data', 'update_announcement_data', 'delete_announcement_data', 'get_students_by_section_and_grade', 
            'search_students_by_name', 'get_section_data', 'get_section_withid', 'create_section_data', 'update_section_data', 'delete_section_data', 'get_grade_data', 
            'get_grade_withid', 'create_grade_data', 'update_grade_data', 'delete_grade_data', 'create_student_attendence_data', 'get_attendance_by_course_section_grade'
            'get_subject_data', 'get_subject_withid', 'create_subject_data', 'update_subject_data', 'delete_subject_data', 'create_student_marks_data', 'get_marks_by_course_section_grade', 
            'get_marks_by_subject', 'get_marks_by_student', 'get_attachments_data', 'create_upload_data', 'get_upload_data', 'update_upload_data', 'get_leave_data', 'create_leave_data'
            'get_login_data', 'get_login_withid', 'create_login_data', 'update_login_data', 'delete_login_data', 'get_fee_details', 'get_fee_detail_by_id', 'create_fee_detail', 
            'update_fee_detail', 'delete_fee_detail', 'total_strength_by_grade', 'get_students_count_by_attendance_present', 'get_students_count_by_attendance_absent', 
            'get_students_count_by_attendance_leave', 'start_workflow', 'complete_step', 'get_workflow_instance', 'get_workflow_instance_steps', 'get_workflow_design_for_instance', 
            'get_max_workflow_instance_id', 'farward_leave_to_principal', 'approve_leave_to_by_sl', 'approve_leave_principal', 'complete_full_workflow',
            'get_tc_data', 'get_tc_withid', 'create_tc_data', 'update_tc_data', 'delete_tc_data', 'get_disciplinary_record_data', 'get_disciplinary_record_withid', 'create_disciplinary_record_data',
            'update_disciplinary_record_data', 'delete_disciplinary_record_data', 'get_exam_data', 'get_exam_withid', 'create_exam_data', 'update_exam_data', 'delete_exam_data', 'get_all_custom_users',
            'get_student_marks_report', 'get_action_required', 'manage_action_required', 'get_upcoming_events', 'create_upcoming_events', 'get_all_students_summary', 'fee_summary_view',
            'get_attendance_by_course_section_grade_json', 'get_examincharge_data', 'get_examincharge_withid', 'create_examincharge_data', 'update_examincharge_data', 'delete_examincharge_data', 
            'get_invigilator_data', 'get_invigilator_withid', 'create_invigilator_data', 'update_invigilator_data', 'delete_invigilator_data', 'reject_leave', 'get_student_report_card', 'get_college_data'
            'get_monthly_login_summary', 'create_fee_structure', 'create_fee_term', 'create_fee_component', 'create_course', 'list_courses', 'get_fee_data', 'approve_structure_principal', 
            'reject_fee_structure']