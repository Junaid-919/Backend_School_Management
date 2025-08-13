from django.urls import path
from .import views
from .views.users_views import LoggedinprofileView


urlpatterns = [

    path('api/get_principal_data/', views.get_principal_data, name='get_principal_data'),

    path('api/create_principal_data/', views.create_principal_data, name='create_principal_data'),

    path('api/update_principal_data/<int:principal_id>/', views.update_principal_data, name='update_principal_data'),

    path('api/delete_principal_data/<int:principal_id>/', views.delete_principal_data, name='delete_principal_data'),


    path('api/get_principal_data_withid/<int:principal_id>/', views.get_principal_data_withid, name='get_principal_data_withid'),

    path('api/get_teacher_data/', views.get_teacher_data, name='get_teacher_data'),

    path('api/create_teacher_data/', views.create_teacher_data, name='create_teacher_data'),

    path('api/update_teacher_data/<int:teacher_id>/', views.update_teacher_data, name='update_teacher_data'),

    path('api/delete_teacher_data/<int:teacher_id>/', views.delete_teacher_data, name='delete_principal_data'),

    path('api/get_teacher_data_withid/<int:teacher_id>/', views.get_teacher_data_withid, name='get_teacher_data_withid'),

    path('api/teacher_attendance_summary/', views.teacher_attendance_summary, name='teacher_attendance_summary'),

    
    
    

    path('api/get_student_data/', views.get_student_data, name='get_student_data'),

    path('api/create_student_data/', views.create_student_data, name='create_student_data'),

    path('api/update_student_data/<int:teacher_id>/', views.update_student_data, name='update_student_data'),

    path('api/delete_student_data/<int:teacher_id>/', views.delete_student_data, name='delete_student_data'),

    path('api/get_student_data_withid/<int:teacher_id>/', views.get_student_data_withid, name='get_student_data_withid'),

    path('api/get_students_by_section_and_grade/', views.get_students_by_section_and_grade, name='get_students_by_section_and_grade'),

    path('api/search_students_by_name/', views.search_students_by_name, name='search_students_by_name'),

    path('api/total_strength_by_grade/', views.total_strength_by_grade, name='total_strength_by_grade'),

    # path('api/total_strength_by_course/', views.total_strength_by_course, name='total_strength_by_course'),

    



    path('api/get_fee_data/', views.get_fee_data, name='get_fee_data'),

    # path('api/create_fee_data/', views.create_fee_data, name='create_fee_data'),

    # path('api/update_fee_data/<int:feestructure_id>/', views.update_fee_data, name='update_fee_data'),

    # path('api/delete_fee_data/<int:feestructure_id>/', views.delete_fee_data, name='delete_fee_data'),

    # path('api/get_fee_data_withid/<int:feestructure_id>/', views.get_fee_data_withid, name='get_fee_data_withid'),
    path('api/approve_structure_principal/<int:instance_id>/', views.approve_structure_principal, name='approve_structure_principal'),



    # path('api/get_course_data/', views.get_course_data, name='get_course_data'),

    # path('api/create_course_data/', views.create_course_data, name='create_course_data'),

    # path('api/update_course_data/<int:course_id>/', views.update_course_data, name='update_course_data'),

    # path('api/delete_course_data/<int:course_id>/', views.delete_course_data, name='delete_course_data'),

    # path('api/get_course_withid/<int:course_id>/', views.get_course_withid, name='get_course_withid'),



    path('api/get_announcement_data/', views.get_announcement_data, name='get_announcement_data'),

    path('api/create_announcement_data/', views.create_announcement_data, name='create_announcement_data'),

    path('api/update_announcement_data/<int:announcement_id>/', views.update_announcement_data, name='update_announcement_data'),

    path('api/delete_announcement_data/<int:announcement_id>/', views.delete_announcement_data, name='delete_announcement_data'),

    path('api/get_announcement_data_withid/<int:announcement_id>/', views.get_announcement_data_withid, name='get_announcement_data_withid'),




    path('api/get_section_data/', views.get_section_data, name='get_section_data'),

    path('api/create_section_data/', views.create_section_data, name='create_section_data'),

    path('api/update_section_data/<int:section_id>/', views.update_section_data, name='update_section_data'),

    path('api/delete_section_data/<int:section_id>/', views.delete_section_data, name='delete_section_data'),

    path('api/get_section_withid/<int:section_id>/', views.get_section_withid, name='get_section_withid'),




    path('api/get_grade_data/', views.get_grade_data, name='get_grade_data'),

    path('api/create_grade_data/', views.create_grade_data, name='create_grade_data'),

    path('api/update_grade_data/<int:grade_id>/', views.update_grade_data, name='update_grade_data'),

    path('api/delete_grade_data/<int:grade_id>/', views.delete_grade_data, name='delete_grade_data'),

    path('api/get_grade_withid/<int:grade_id>/', views.get_grade_withid, name='get_grade_withid'),


    path('api/get_college_data/', views.get_college_data, name='get_college_data'),




    path('api/create_student_attendence_data/', views.create_student_attendence_data, name='create_student_attendence_data'),

    path('api/get_attendance_by_course_section_grade/', views.get_attendance_by_course_section_grade, name='get_attendance_by_course_section_grade'),

    path('api/get_students_count_by_attendance_present/', views.get_students_count_by_attendance_present, name='get_students_count_by_attendance_present'),

    path('api/get_students_count_by_attendance_absent/', views.get_students_count_by_attendance_absent, name='get_students_count_by_attendance_absent'),

    path('api/get_students_count_by_attendance_leave/', views.get_students_count_by_attendance_leave, name='get_students_count_by_attendance_leave'),

    path('api/get_student_report_card/<int:student_id>/', views.get_student_report_card, name='get_student_report_card'),



    path('api/get_subject_data/', views.get_subject_data, name='get_subject_data'),

    path('api/create_subject_data/', views.create_subject_data, name='create_subject_data'),

    path('api/update_subject_data/<int:subject_id>/', views.update_subject_data, name='update_subject_data'),

    path('api/delete_subject_data/<int:subject_id>/', views.delete_subject_data, name='delete_subject_data'),

    path('api/get_subject_withid/<int:subject_id>/', views.get_subject_withid, name='get_subject_withid'),


    path('api/create_student_marks_data/', views.create_student_marks_data, name='create_student_marks_data'),

    path('api/get_marks_by_course_section_grade/', views.get_marks_by_course_section_grade, name='get_marks_by_course_section_grade'),

    path('api/get_marks_by_subject/', views.get_marks_by_subject, name='get_marks_by_subject'),

    path('api/get_marks_by_student/', views.get_marks_by_student, name='get_marks_by_student'),



    path('api/get_attachments_data/', views.get_attachments_data, name='get_attachments_data'),



    path('api/create_upload_data/', views.create_upload_data, name='create_upload_data'),
    path('api/get_upload_data/', views.get_upload_data, name='get_upload_data'),
    path('api/update_upload_data/<int:upload_id>/', views.update_upload_data, name='update_upload_data'),


    path('api/get_leave_data/', views.get_leave_data, name='get_leave_data'),

    path('api/create_leave_data/', views.create_leave_data, name='create_leave_data'),
    path('api/farward_leave_to_principal/<int:instance_id>/', views.farward_leave_to_principal, name='farward_leave_to_principal'),

    path('api/approve_leave_to_by_sl/<int:instance_id>/', views.approve_leave_to_by_sl, name='farward_leave_to_principal'),
    path('api/approve_leave_principal/<int:instance_id>/', views.approve_leave_principal, name='farward_leave_to_principal'),
    path('api/reject_leave/<int:instance_id>/', views.reject_leave, name='farward_leave_to_principal'),



    path('api/get_login_data/', views.get_login_data, name='get_login_data'),

    path('api/create_login_data/', views.create_login_data, name='create_login_data'),

    path('api/update_login_data/<int:login_id>/', views.update_login_data, name='update_login_data'),

    path('api/delete_login_data/<int:login_id>/', views.delete_login_data, name='delete_login_data'),

    path('api/get_login_withid/<int:login_id>/', views.get_login_withid, name='get_login_withid'),



    path('api/get_fee_details/', views.get_fee_details, name='get_fee_details'),

    path('api/create_fee_detail/', views.create_fee_detail, name='create_fee_detail'),

    path('api/update_fee_detail/<int:fee_detail_id>/', views.update_fee_detail, name='update_fee_detail'),

    path('api/delete_fee_detail/<int:fee_detail_id>/', views.delete_fee_detail, name='delete_fee_detail'),

    path('api/get_fee_detail_by_id/<int:fee_detail_id>/', views.get_fee_detail_by_id, name='get_fee_detail_by_id'),




    path('api/start_workflow/<int:workflow_design_id>/', views.start_workflow, name='start_workflow'),

    path('api/complete_step/<int:instance_id>/', views.complete_step, name='complete_step'),

    path('api/complete_full_workflow/<int:instance_id>/', views.complete_full_workflow, name='complete_step'),

    path('api/get_workflow_instance/<int:instance_id>/', views.get_workflow_instance, name='complete_step'),

    path('api/get_workflow_instance_steps/<int:instance_id>/', views.get_workflow_instance_steps, name='complete_step'),

    path('api/get_workflow_design_for_instance/<int:instance_id>/', views.get_workflow_design_for_instance, name='complete_step'),

    path('api/get_max_workflow_instance_id/', views.get_max_workflow_instance_id, name='complete_step'),

    
    
    
    
    path('api/get_tc_data/', views.get_tc_data, name='get_tc_data'),

    path('api/create_tc_data/', views.create_tc_data, name='get_tc_withid'),

    path('api/update_tc_data/<int:tc_id>/', views.update_tc_data, name='update_course_data'),

    path('api/delete_tc_data/<int:tc_id>/', views.delete_tc_data, name='delete_course_data'),

    path('api/get_tc_withid/<int:tc_id>/', views.get_tc_withid, name='get_course_withid'),




    path('api/get_disciplinary_record_data/', views.get_disciplinary_record_data, name='get_tc_data'),

    path('api/create_disciplinary_record_data/', views.create_disciplinary_record_data, name='get_tc_withid'),

    path('api/update_disciplinary_record_data/<int:disciplinary_record_id>/', views.update_disciplinary_record_data, name='update_course_data'),

    path('api/delete_disciplinary_record_data/<int:disciplinary_record_id>/', views.delete_disciplinary_record_data, name='delete_course_data'),

    path('api/get_disciplinary_record_withid/<int:disciplinary_record_id>/', views.get_disciplinary_record_withid, name='get_course_withid'),





    path('api/get_exam_data/', views.get_exam_data, name='get_tc_data'),

    path('api/create_exam_data/', views.create_exam_data, name='get_tc_withid'),

    path('api/update_exam_data/<int:exam_id>/', views.update_exam_data, name='update_course_data'),

    path('api/delete_exam_data/<int:exam_id>/', views.delete_exam_data, name='delete_course_data'),

    path('api/get_exam_withid/<int:exam_id>/', views.get_exam_withid, name='get_course_withid'),



    path('api/get_all_custom_users/', views.get_all_custom_users, name='get_course_withid'),


    path('api/get_student_marks_report/', views.get_student_marks_report, name='get_course_withid'),

    path('api/get_attendance_by_course_section_grade_json/', views.get_attendance_by_course_section_grade_json, name='get_course_withid'),



    path('api/get_action_required/', views.get_action_required, name='get_attendance_by_course_section_grade_json'),

    path('api/manage_action_required/', views.manage_action_required, name='get_attendance_by_course_section_grade_json'),


    path('api/get_upcoming_events/', views.get_upcoming_events, name='get_attendance_by_course_section_grade_json'),
    
    path('api/create_upcoming_events/', views.create_upcoming_events, name='get_attendance_by_course_section_grade_json'),


    path('api/get_all_students_summary/', views.get_all_students_summary, name='get_attendance_by_course_section_grade_json'),

    path('api/fees_summary_view/', views.fee_summary_view, name='get_attendance_by_course_section_grade_json'),





    path('api/get_examincharge_data/', views.get_examincharge_data, name='get_tc_data'),

    path('api/create_examincharge_data/', views.create_examincharge_data, name='get_tc_withid'),

    path('api/update_examincharge_data/<int:examincharge_id>/', views.update_examincharge_data, name='update_course_data'),

    path('api/delete_examincharge_data/<int:examincharge_id>/', views.delete_examincharge_data, name='delete_course_data'),

    path('api/get_examincharge_withid/<int:examincharge_id>/', views.get_examincharge_withid, name='get_course_withid'),






    path('api/get_invigilator_data/', views.get_invigilator_data, name='get_tc_data'),

    path('api/create_invigilator_data/', views.create_invigilator_data, name='get_tc_withid'),

    path('api/update_invigilator_data/<int:invigilator_id>/', views.update_invigilator_data, name='update_course_data'),

    path('api/delete_invigilator_data/<int:invigilator_id>/', views.delete_invigilator_data, name='delete_course_data'),

    path('api/get_invigilator_withid/<int:invigilator_id>/', views.get_invigilator_withid, name='get_course_withid'),


    path('api/LoggedinprofileView/', LoggedinprofileView.as_view(), name='get_course_withid'),


    path('api/get_monthly_login_summary/', views.get_monthly_login_summary, name='get_course_withid'),

    path('api/create_fee_structure/', views.create_fee_structure, name='get_course_withid'),

    path('api/create_fee_term/', views.create_fee_term, name='get_course_withid'),

    path('api/create_fee_component/', views.create_fee_component, name='get_course_withid'),

    path('api/create_course/', views.create_course, name='get_course_withid'),

    path('api/list_courses/', views.list_courses, name='get_course_withid'),


     path('api/reject_fee_structure/', views.reject_fee_structure, name='get_course_withid'),

]