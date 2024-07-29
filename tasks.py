from crewai import Task
from .agents import (product_manager,
                     technical_lead,
                     lead_developer,
                     software_developer,
                     test_engineer,
                     qa_lead,
                     documentation_specialist)

# PD Tasks

task_collect_review = Task(
    description='Gather all incoming user requests, feature suggestions, and bug reports from various channels.',
    agent=product_manager,
    expected_output='A consolidated list of user requests with initial categorization (e.g., feature requests, bug reports).'
)

task_analyze_requirements = Task(
    description='Review and analyze the gathered requests to understand the requirements and their implications.',
    agent=product_manager,
    expected_output='A detailed analysis report highlighting key requirements, dependencies, and any potential impacts.'
)

task_create_specifications = Task(
    description='Develop clear, detailed specifications based on the analyzed requirements, including user stories and acceptance criteria.',
    agent=product_manager,
    expected_output='A comprehensive specification document outlining the feature or bug fix, including user stories, functional requirements, and acceptance criteria.'
)

task_prioritize_requests = Task(
    description='Evaluate and prioritize the requests based on business value, user impact, and feasibility.',
    agent=product_manager,
    expected_output='A prioritized list of requests with justification for their ranking.'
)

task_coordinate_technical_lead = Task(
    description='Work closely with the Technical Lead to ensure that the specifications are feasible and align with the system architecture.',
    agent=product_manager,
    expected_output='Meeting notes or a summary of discussions and agreements with the Technical Lead regarding the design and feasibility of the specifications.'
)

task_update_documentation = Task(
    description='Ensure that all specifications and requirements are properly documented and updated in the requested implementation.',
    agent=product_manager,
    expected_output='Updated project documentation reflecting the new specifications and requirements.'
)

task_review_progress = Task(
    description='Monitor the progress of the implementation to ensure it aligns with the specifications and adjust priorities or requirements as needed.',
    agent=product_manager,
    expected_output='Status reports and feedback on the implementation progress, including any necessary adjustments or clarifications.'
)

# Tech Lead Tasks
task_design_solution = Task(
    description='Design a solution based on the specifications provided by the Product Manager. This includes system architecture, design patterns, and key components.',
    agent=technical_lead,
    expected_output='A detailed design document outlining the proposed solution, including system architecture, design patterns, and key components.'
)

task_create_development_plan = Task(
    description='Create a development plan that breaks down the solution into actionable tasks.',
    agent=technical_lead,
    expected_output='A comprehensive development plan that includes a task breakdown and dependencies.'
)

task_review_and_approve_technical_feasibility = Task(
    description='Review the design and development plan for technical feasibility. Ensure that the proposed solution can be implemented within the constraints of the existing system architecture.',
    agent=technical_lead,
    expected_output='A feasibility report that confirms the design’s practicality or suggests necessary adjustments.'
)

task_communicate_with_development_team = Task(
    description='Communicate the design and development plan to the development team, ensuring that all team members understand the requirements, tasks, and deadlines.',
    agent=technical_lead,
    expected_output='Meeting notes or communication logs documenting the design and development plan, along with feedback from the development team.'
)

task_manage_technical_dependencies = Task(
    description='Identify and manage technical dependencies related to the solution. Coordinate with other teams or components that might be impacted or need to be integrated.',
    agent=technical_lead,
    expected_output='A list of technical dependencies and a plan for managing and integrating them into the project.'
)

task_review_implementation_progress = Task(
    description='Monitor and review the progress of the implementation to ensure that it aligns with the design and development plan. Provide guidance and make adjustments as needed.',
    agent=technical_lead,
    expected_output='Progress reports and updates on the implementation, including any issues encountered and recommendations for adjustments.'
)

task_update_design_and_plan_as_needed = Task(
    description='Update the design and development plan based on feedback, changes in requirements, or any unforeseen challenges that arise during implementation.',
    agent=technical_lead,
    expected_output='Revised design and development documents that reflect any changes or adjustments made during the implementation process.'
)

task_ensure_implementation_quality = Task(
    description='Ensure that the implementation adheres to quality standards and the design specifications. Perform code reviews and oversee testing to guarantee that the final solution meets the required standards.',
    agent=technical_lead,
    expected_output='Quality assurance reports and documentation demonstrating that the implementation meets design specifications and quality standards.'
)

task_document_technical_decisions = Task(
    description='Document all significant technical decisions and changes made during the design and development process to provide a clear record for future reference.',
    agent=technical_lead,
    expected_output='A documentation of technical decisions, including rationale and impact, to be used for future reference and audits.'
)

# Lead Developer Tasks
task_oversee_development_process = Task(
    description='Monitor and oversee the entire development process to ensure that all aspects of implementation align with the design specifications and project requirements.',
    agent=lead_developer,
    expected_output='A comprehensive development progress report detailing alignment with design, adherence to standards, and any issues encountered.'
)

task_guide_development_team = Task(
    description='Provide guidance and support to the development team, ensuring they understand the design specifications, follow best practices, and resolve any issues that arise.',
    agent=lead_developer,
    expected_output='Documentation of the guidance and support provided, including any training materials, instructions, or advice given to the team.'
)

task_conduct_code_reviews = Task(
    description='Conduct thorough code reviews to ensure the code adheres to quality standards, follows best practices, and aligns with the design specifications.',
    agent=lead_developer,
    expected_output='Detailed code review reports highlighting issues, improvements, and confirmations of adherence to design and quality standards.'
)

task_manage_technical_debt = Task(
    description='Identify and manage technical debt that arises during development to maintain the long-term health and performance of the codebase.',
    agent=lead_developer,
    expected_output='A list of technical debt items with a plan for addressing them, including prioritization and strategies for remediation.'
)

task_monitor_project_milestones = Task(
    description='Track the progress of the project against milestones and deadlines, making necessary adjustments to keep the project on track and meet delivery goals.',
    agent=lead_developer,
    expected_output='Status reports on project milestones showing progress, delays, and any adjustments made to the project plan.'
)


task_resolve_technical_issues = Task(
    description='Address and resolve technical issues that arise during the development process to ensure smooth progress and successful implementation.',
    agent=lead_developer,
    expected_output='Issue resolution reports detailing problems encountered, and solutions implemented.'
)

task_document_development_decisions = Task(
    description='Document significant development decisions, including design choices, changes to the plan, and any deviations from the original requirements.',
    agent=lead_developer,
    expected_output='Comprehensive documentation of development decisions, including rationale and impact on the project.'
)

# Software Developer Tasks
task_implement_solution = Task(
    description='Implement the solution based on the design and specifications provided. Ensure the code aligns with the design and meets all requirements.',
    agent=software_developer,
    expected_output='Fully functional code that meets the design specifications and requirements, demonstrating adherence to coding standards and quality.'
)

task_write_unit_tests = Task(
    description='Write unit tests to verify that individual components of the solution work as intended. Ensure comprehensive coverage of all code paths.',
    agent=software_developer,
    expected_output='A suite of unit tests with clear results showing that all components of the solution function correctly and edge cases are handled.'
)

task_refactor_code = Task(
    description='Refactor code to improve readability, maintainability, and performance while ensuring that functionality remains unchanged.',
    agent=software_developer,
    expected_output='Refactored code that is cleaner and more efficient, with improved documentation and no change in functionality.'
)

task_fix_bugs = Task(
    description='Identify and fix any bugs or issues that arise during development or testing. Ensure that the solution functions as expected and meets quality standards.',
    agent=software_developer,
    expected_output='A list of bugs or issues identified and resolved, with corresponding fixes applied and verified through testing.'
)

task_document_code = Task(
    description='Document the implemented code, including explanations of functionality, usage, and any design decisions made during development.',
    agent=software_developer,
    expected_output='Comprehensive code documentation that includes descriptions of functionality, usage examples, and explanations of design decisions.'
)

task_collaborate_with_team = Task(
    description='Collaborate with other team members, including developers and the lead developer, to ensure that the implementation aligns with the overall project goals and integrates well with other components.',
    agent=software_developer,
    expected_output='Records of collaboration, including meeting notes, feedback provided, and integration details that show alignment with project goals.'
)

task_adhere_to_code_standards = Task(
    description='Ensure that the implemented code adheres to established coding standards and best practices, including style guidelines and design patterns.',
    agent=software_developer,
    expected_output='Code that meets established coding standards and best practices, with evidence of adherence such as code review comments or style check results.'
)

task_optimize_performance = Task(
    description='Optimize the performance of the implemented solution by identifying and addressing any bottlenecks or inefficiencies.',
    agent=software_developer,
    expected_output='Performance optimization reports showing improvements in efficiency and performance, with before and after metrics as applicable.'
)

task_integrate_with_other_components = Task(
    description='Integrate the solution with other system components or services as required, ensuring compatibility and seamless operation within the overall system.',
    agent=software_developer,
    expected_output='Successful integration of the solution with other components, including any necessary adjustments or configurations to ensure compatibility.'
)