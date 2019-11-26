# 2019 Michigan IT Symposium

The Michigan IT Symposium is an annual event to help create connections between community members, while highlighting the innovation and ingenuity occurring across all of the U-M campuses. The event is open to all University of Michigan IT and technology professionals and advocates and includes multiple types of interactions, including plenary and breakout events.

## Automated Testing and Deployment of Infrastructure and Applications using Ansible and Molecule
Ansible is an open-source automation tool that is being used across the university and worldwide for configuration management and automated application deployment. Automation with Ansible saves time and minimizes errors, allowing our infrastructure to be declarative. We can know the exact state of our infrastructure, how an application was installed, and can rapidly scale resources with minimal direct interaction.

We have been leveraging Ansible across LSA TS and HITS. In this session, we will share the ways Ansible has helped minimize the time and resources needed for post-build configuration and ongoing maintenance such as software patching. We will provide examples of common administrative tasks that can be simplified, and combined, using Ansible.

In addition, we will take a deep dive into Molecule, the testing framework for Ansible, and show how it is being used to test configurations, deployments, and software lifecycle paths in local containers and/or virtual machines before impacting real-world systems. We will describe our techniques for debugging and testing using Molecule, while sharing the common challenges we faced along the way.

## Repo layout
* [molecule.pdf](Michigan_IT_Symposium2019/molecule.pdf): Molecule half of the presentation
* [it_symposium role](Michigan_IT_Symposium2019/it_symposium): Molecule 101 role used in demo
* [docker-molecule.yml](Michigan_IT_Symposium2019/docker-molecule.yml): Sample molecule.yml for testing multiple environments using Docker containers
* [virtualbox-molecule.yml](Michigan_IT_Symposium2019/virtualbox-molecule.yml): Sample molecule.yml for testing using vagrant and VirtualBox VMs
* [gitlabCI-molecule.yml](Michigan_IT_Symposium2019/gitlabCI-molecule.yml): Sample .gitlab-ci.yml to integrate molecule into a GitLab CI/CD pipeline
