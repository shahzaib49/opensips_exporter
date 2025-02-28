# OpenSIPS Exporter

**Version:** 0.1.0  
**Author:** Shah Zaib Rana

## Overview

The **OpenSIPS Exporter** is a Prometheus exporter for OpenSIPS MI (Management Interface) commands. It uses the `opensipscli` library to query OpenSIPS for metrics and exposes them via an HTTP server for Prometheus to scrape.

This package is designed to be modular and extensible. Currently, it supports two main categories of metrics:
- **Load Balancer Metrics:** Retrieves data from the `mi lb_list` command.
- **Profile Metrics:** Retrieves data from the `mi list_all_profiles` and `mi profile_get_size profilename` commands.

## Current Metrics

### Load Balancer Metrics

- **opensips_lb_allowed_load**  
  - **Description:** Allowed capacity (max value) for each load-balancing resource.
  - **Labels:**  
    - `uri`: The destination URI (e.g., `sip:10.0.44.74:5060`)
    - `id`: The destination identifier
    - `group`: The group number
    - `enabled`: Whether the destination is enabled (`yes` or `no`)
    - `auto_reenable`: Auto reenable status (converted dashes replaced by underscores)
    - `resource_name`: The name of the resource (e.g., `application`)

- **opensips_lb_current_load**  
  - **Description:** The current load value for each load-balancing resource.
  - **Labels:** Same as above.

### Profile Metrics

- **profile_call_count**  
  - **Description:** The call count for each profile, as returned by the `mi profile_get_size profilename` command.
  - **Labels:**  
    - `profile_name`: The name of the profile (e.g., `trunkCalls`)
    - `profile_value`: The profile's value (or `"none"` if no value is present)

## Package Structure

