# Activity Summary

Portfolio Activity: **Create a VPC using Cloud Shell**, a hands-on lab from the "Introduction to Security Principles in Cloud Computing" course of the Google Cloud Cybersecurity Certificate.

I provisioned and verified a custom Virtual Private Cloud (VPC) network in **Google Cloud** using the `gcloud` command line in Cloud Shell, documenting each command, its output, and my reasoning — including a real error and how I resolved it.

## Objectives accomplished

- Configured the Cloud Shell session: listed the active account (`gcloud auth list`) and set the active project (`gcloud config set project`).
- **Task 1 — Create a network**: created a custom-mode VPC network (`labnet`) with `gcloud compute networks create --subnet-mode=custom`. Hit and resolved a real error (`required property [project] is not currently set`) by setting the active project first.
- **Task 2 — Create a subnet**: created subnet `labnet-sub` in region `us-east1` with range `10.0.0.0/28`.
- **Task 3 — View networks**: listed networks and explained the difference between the custom `labnet` (SUBNET_MODE CUSTOM) and the default network (AUTO).
- **Task 4 — List subnets**: verified the created subnet with `gcloud compute networks subnets list`.

## Folder Structure and Status

- `LabSolution.md`: step-by-step lab walkthrough with the executed `gcloud` commands, their outputs, and explanations (covers network and subnet creation and verification, Tasks 1–4).
- `image.png`: Cloud Shell screenshot.

## Tools

Google Cloud Platform, Cloud Shell, `gcloud` CLI (Compute Engine networking: VPC networks and subnets), custom-mode VPC, CIDR subnetting.
