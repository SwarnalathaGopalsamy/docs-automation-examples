# Writing Samples

These are original documentation samples written to demonstrate my technical 
writing skills. They reflect the types of documentation I create professionally, 
adapted for a fictional product to protect confidentiality.

---

## Sample 1: Getting Started with FlowTrack WMS

**Type:** User Guide  
**Audience:** New enterprise users  
**Product:** FlowTrack — a fictional warehouse management SaaS platform

### Overview
FlowTrack helps warehouse teams manage inventory, track orders, and automate 
workflows from a single dashboard.

### Step 1: Log in to FlowTrack
1. Open your browser and go to `app.flowtrack.io`
2. Enter your company email and temporary password from your welcome email
3. Click **Sign In**
4. When prompted, set a new password and click **Save**

### Step 2: Set Up Your Warehouse Profile
1. Click your profile icon in the top right corner
2. Select **Warehouse Settings**
3. Enter your warehouse name, location, and operating hours
4. Click **Save Settings**

### Step 3: Add Your First Inventory Item
1. From the dashboard, click **Inventory** in the left navigation
2. Click **+ Add Item**
3. Fill in the item name, SKU, quantity, and storage zone
4. Click **Save**

> **Tip:** Use the bulk import option under **Inventory → Import CSV** to add 
> multiple items at once.

---

## Sample 2: FlowTrack v2.4 Release Notes

**Type:** Release Notes  
**Audience:** Existing users and administrators  

### What's New in v2.4

**New Features**
- **Smart Routing Engine** — Automatically assigns optimal pick paths for 
  warehouse staff based on order priority and zone layout
- **Multi-warehouse Dashboard** — View and manage inventory across multiple 
  warehouse locations from a single dashboard

**Improvements**
- Improved search performance in the Inventory module — results now load 
  up to 40% faster
- Updated onboarding checklist with clearer step descriptions

**Bug Fixes**
- Fixed an issue where order status did not update after manual override
- Resolved a display error in the Reports module on smaller screen sizes

**Known Issues**
- Export to PDF in the Reports module may time out for datasets exceeding 
  10,000 rows. Workaround: filter by date range before exporting.

---

## Sample 3: ClickHelp CMS — Configuration Reference

**Type:** Reference Documentation  
**Audience:** Documentation administrators  

### Publication Settings

| Setting | Description | Default |
|---|---|---|
| Publication URL | The unique URL slug for your documentation portal | Required |
| Access Level | Controls who can view the publication: Public, Private, or Password-protected | Public |
| Version Label | Display label shown to readers for this version | Latest |
| Search Indexing | Enables full-text search across all topics | Enabled |

### Content Reuse Settings

| Setting | Description |
|---|---|
| Snippet Library | Reusable content blocks that can be inserted across multiple topics |
| Variable Sets | Define product names, versions, or terms that update globally |
| Conditional Tags | Show or hide content blocks based on audience or product version |

### Metadata Fields

- **Topic Title** — Displayed in navigation and browser tab
- **Meta Description** — Used for search engine previews
- **Tags** — Keywords for internal search optimization
- **Author** — Tracks content ownership for review workflows

---

## Sample 4: FlowTrack WMS — Troubleshooting Guide

**Type:** Troubleshooting Guide  
**Audience:** End users and system administrators  
**Product:** FlowTrack — a fictional warehouse management SaaS platform

### Overview

This guide helps users resolve common issues encountered while using 
FlowTrack WMS.

---

### Issue 1: Unable to Log In

**Symptoms:**
- Login page displays an error message
- Page refreshes without logging in
- Account appears locked

**Possible Causes and Solutions:**

| Cause | Solution |
|---|---|
| Incorrect password | Click **Forgot Password** on the login page and follow the reset steps |
| Account locked after failed attempts | Contact your system administrator to unlock the account |
| Browser cache issue | Clear your browser cache and cookies, then try again |
| VPN not connected | Ensure you are connected to your company VPN before logging in |

---

### Issue 2: Inventory Items Not Updating

**Symptoms:**
- Stock levels appear outdated
- Recently added items are not visible
- Inventory count does not match physical stock

**Possible Causes and Solutions:**

| Cause | Solution |
|---|---|
| Sync delay | Wait 5 minutes and refresh the page |
| Bulk import failed | Go to **Inventory → Import History** and check for import errors |
| Filter applied | Check if an active filter is hiding items under **Inventory → Filters** |
| Insufficient permissions | Contact your administrator to verify your access level |

> **Tip:** Always check the **Activity Log** under **Settings → Audit Trail** 
> to track recent changes to inventory records.

---

### Issue 3: Reports Not Generating

**Symptoms:**
- Report page shows a loading spinner indefinitely
- Error message: "Report generation failed"
- Downloaded report file is empty

**Possible Causes and Solutions:**

| Cause | Solution |
|---|---|
| Large date range selected | Reduce the date range and try again |
| Scheduled maintenance | Check the FlowTrack status page for ongoing maintenance |
| Browser timeout | Use the **Schedule Report** option to receive it by email instead |

---

## Sample 5: FlowTrack WMS — User Onboarding Guide

**Type:** Onboarding Guide  
**Audience:** New users joining an enterprise warehouse team  
**Product:** FlowTrack — a fictional warehouse management SaaS platform

### Overview

Welcome to FlowTrack! This guide walks you through everything you need 
to get started in your first week.

---

### Day 1 — Access and Setup

**Step 1: Activate your account**
1. Check your work email for a FlowTrack welcome message
2. Click **Activate Account** in the email
3. Set your password and click **Save**
4. Log in at `app.flowtrack.io`

**Step 2: Complete your profile**
1. Click your name in the top right corner
2. Select **My Profile**
3. Add your job title, department, and contact number
4. Click **Save Profile**

**Step 3: Explore the dashboard**

| Section | Purpose |
|---|---|
| **Inventory** | View and manage stock levels across all zones |
| **Orders** | Track inbound and outbound orders |
| **Reports** | Generate and schedule performance reports |
| **Settings** | Manage your profile and notification preferences |

---

### Day 2 — Core Tasks

**Processing your first order:**
1. Go to **Orders → Inbound Orders**
2. Click the order number to open it
3. Review the item list and quantities
4. Click **Confirm Receipt** when items are physically received
5. The inventory levels update automatically

> **Note:** Always verify physical quantities before confirming receipt. 
> Discrepancies must be reported to your supervisor within 24 hours.

---

### Day 3 — Tips for Success

- Use the **Search** bar at the top to quickly find any item, order, or report
- Set up **Email Notifications** under Settings to stay updated on order status
- Bookmark your most used reports under **Reports → Favourites**
- Reach out to your team lead if you encounter any access issues

---

## Sample 6: FlowTrack WMS — Standard Operating Procedure

**Type:** SOP (Standard Operating Procedure)  
**Audience:** Warehouse operations team  
**Product:** FlowTrack — a fictional warehouse management SaaS platform

---

**Document ID:** SOP-WMS-001  
**Version:** 1.2  
**Last Reviewed:** March 2026  
**Owner:** Warehouse Operations Team  

---

### Purpose

This SOP defines the standard process for receiving, recording, and 
confirming inbound inventory in FlowTrack WMS to ensure accurate stock 
levels and audit compliance.

### Scope

This procedure applies to all warehouse staff responsible for processing 
inbound shipments.

### Prerequisites

- Active FlowTrack account with Inventory Editor access
- Completed FlowTrack onboarding training
- Access to the physical receiving area

---

### Procedure

**Step 1: Verify the shipment**
1. Receive the physical shipment at the warehouse dock
2. Match the delivery note against the Purchase Order (PO) in FlowTrack
3. Go to **Orders → Inbound Orders** and locate the corresponding PO
4. Verify item names, SKUs, and quantities

**Step 2: Record received items**
1. Click the PO number to open the order
2. For each item received, enter the actual quantity in the **Received Qty** field
3. Note any damaged or missing items in the **Remarks** field
4. Click **Save Draft** — do not confirm until all items are verified

**Step 3: Report discrepancies**
1. If quantities do not match, click **Flag Discrepancy**
2. Enter the reason and actual quantity received
3. Notify your supervisor immediately
4. Do not proceed until the discrepancy is resolved

**Step 4: Confirm receipt**
1. Once all items are verified, click **Confirm Receipt**
2. The system updates inventory levels automatically
3. A confirmation email is sent to the procurement team

---

### Quality Checks

| Check | Frequency | Responsible |
|---|---|---|
| Verify PO against delivery note | Every shipment | Receiving staff |
| Check for damaged items | Every shipment | Receiving staff |
| Supervisor review of discrepancies | As needed | Supervisor |
| Monthly audit of SOP compliance | Monthly | Team Lead |

---

### Related Documents

- SOP-WMS-002: Outbound Shipment Processing
- SOP-WMS-003: Inventory Cycle Count Procedure
- FlowTrack User Guide: Getting Started

---

## Sample 7: FlowTrack WMS — Knowledge Base Article

**Type:** Knowledge Base Article  
**Audience:** End users  
**Product:** FlowTrack — a fictional warehouse management SaaS platform

**Article ID:** KB-WMS-0042  
**Last Updated:** March 2026  
**Category:** Inventory Management  

---

### How to Transfer Stock Between Warehouse Zones in FlowTrack

#### Overview

A zone transfer moves inventory from one storage zone to another within 
the same warehouse. Use this when reorganizing stock locations or 
balancing capacity across zones.

---

#### Before You Begin

- Ensure you have **Inventory Editor** access in FlowTrack
- Confirm the destination zone has sufficient available capacity
- Have the item SKU or name ready

---

#### Steps

1. Log in to FlowTrack at `app.flowtrack.io`
2. Go to **Inventory** in the left navigation
3. Search for the item using the SKU or item name
4. Click the item name to open the item details
5. Click **Transfer Stock**
6. In the **Transfer Stock** dialog:
   - Select the **Source Zone** (current location)
   - Select the **Destination Zone** (new location)
   - Enter the quantity to transfer
7. Click **Confirm Transfer**
8. The system updates both zone quantities immediately

---

#### What to Expect After Transfer

- The source zone quantity decreases by the transferred amount
- The destination zone quantity increases by the same amount
- A transfer record is logged under **Settings → Audit Trail**
- No email notification is sent for zone transfers by default

---

#### Related Articles

- How to Add a New Inventory Item
- How to Set Up Warehouse Zones
- How to Export Inventory Reports