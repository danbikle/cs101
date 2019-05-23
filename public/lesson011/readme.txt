lesson011/readme.txt

redshift

https://us-west-2.console.aws.amazon.com/redshift/home?region=us-west-2

https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-prereq.html

http://www.sql-workbench.net/Workbench-Build124.zip

unzip...

~/sqlwb/sqlworkbench.sh

out of order:
https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html

https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/1.2.16.1027/RedshiftJDBC42-1.2.16.1027.jar

~/sqlwb/ext/RedshiftJDBC42-1.2.16.1027.jar


https://console.aws.amazon.com/iam/


In the left navigation pane, choose Roles.

Choose Create role

In the AWS Service group, choose Redshift.

Under Select your use case, choose Redshift - Customizable then choose Next: Permissions.

On the Attach permissions policies page, choose AmazonS3ReadOnlyAccess, and then choose Next: Review.

For Role name, type a name for your role. For this tutorial, type myRedshiftRole.

Review the information, and then choose Create Role.

Choose the role name of the role you just created.

Copy the Role ARN to your clipboard

my arn:

arn:aws:iam::448496253599:role/myRedshiftRole

now I should create a cluster:


https://console.aws.amazon.com/redshift/

select US West (Oregon).

choose Quick launch cluster.

On the Cluster specifications page, enter the following values and then choose Launch cluster:

    Node type: Choose dc2.large.

    Number of compute nodes: Keep the default value of 2.

    Master user name: Keep the default value of awsuser.

    Master user password and Confirm password: Enter a password for the master user account.
pass: Dan12345

    Database port: Accept the default value of 5439.

    Available IAM roles: Choose myRedshiftRole.

Cluster redshift-cluster-1 is being created. Your cluster may take a few minutes to launch.



    If you launched your cluster in the EC2-VPC platform, follow the steps in To Configure the VPC Security Group (EC2-VPC Platform).

    If you launched your cluster in the EC2-Classic platform, follow the steps in To Configure the Amazon Redshift Security Group.

I checked my cluster here:

https://us-west-2.console.aws.amazon.com/redshift

I saw this:

Cluster Properties
VPC IDVPC ID of the cluster subnet group associated with this cluster.	
vpc-14eb2d6c ( View VPCs )

So, my cluster is in  the EC2-VPC platform



How to Configure the VPC Security Group (EC2-VPC Platform):

visit
https://us-west-2.console.aws.amazon.com/redshift
choose Clusters.
click redshift-cluster-1

I should land in Configuration tab.

Find my security group

I saw this link:

VPC security groupsList of VPC Security Groups associated with this cluster.	
default (sg-b0e2acc3)
 ( active )

I clicked it

I landed here:

https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#SecurityGroups:search=sg-b0e2acc3;sort=groupId

I clicked the Inbound tab. 

I clicked button: "Edit"

I clicked button: "Add Rule"

I entered the following

    Type: Custom TCP Rule.

    Protocol: TCP.

    Port Range: type the same port number that you used when you launched the cluster. The default port for Amazon Redshift is 5439, but your port might be different.

    Source: select Custom IP, then type 0.0.0.0/0.
I clicked Save.



How To Get Your Connection String

    In the Amazon Redshift console, in the navigation pane, choose Clusters.

    Choose redshift-cluster-1 to open it, I should land in the Configuration tab.

    I copied the JDBC URL of the cluster:
    
jdbc:redshift://redshift-cluster-1.cmea74qjjc8h.us-west-2.redshift.amazonaws.com:5439/dev    



how To Connect from SQL Workbench/J to Your Cluster

    Open SQL Workbench/J.

    Choose File, and then choose Connect window.

    Choose Create a new connection profile.

    In the New profile text box, type a name for the profile.

    Choose button "Manage Drivers" at bottom. The Manage Drivers dialog should open.

    Choose the Create a new entry button. In the Name text box, type a name for the driver.

    I Interacted with the form until it contained this info:
    
    Name: Amazon Redshift
    Library: /home/dan/sqlwb/ext/RedshiftJDBC42-1.2.16.1027.jar
    Classname: com.amazon.redshift.jdbc.Driver
    Sample URL: jdbc:redshift://endpoint:port/database
    
I clicked okay.

The window disappeared.

I landed in the Select Connection Profile form-window.

The Driver field allowed me to pulldown value: "Amazon Redshift (com.amazon.redshift.jdbc.Driver)"

In the URL field I pasted a string:

  jdbc:redshift://redshift-cluster-1.cmea74qjjc8h.us-west-2.redshift.amazonaws.com:5439/dev

In Username field I typed:  awsuser

password: Dan12345

I checked box: Autocommit

At upper left I clicked the floppy to save my work.

At lower right I clicked button: "OK"

It did a tiny bounce and then disappeared.

I landed in window: "SQL Workbench/J dan1"

In statement1 tab I entered some sql:

create table dropme
(
userid integer,
username char(8),
firstname varchar(30),
lastname varchar(30)
);
	
insert into dropme values(1,'dan1', 'dan', 'bikle');

select * from dropme;

I mouse-selected above syntax.

I clicked the blue-run-arrow at upper left.

The sql worked well!

I entered and ran this sql:

create table users(
	userid integer not null distkey sortkey,
	username char(8),
	firstname varchar(30),
	lastname varchar(30),
	city varchar(30),
	state char(2),
	email varchar(100),
	phone char(14),
	likesports boolean,
	liketheatre boolean,
	likeconcerts boolean,
	likejazz boolean,
	likeclassical boolean,
	likeopera boolean,
	likerock boolean,
	likevegas boolean,
	likebroadway boolean,
	likemusicals boolean);

create table venue(
	venueid smallint not null distkey sortkey,
	venuename varchar(100),
	venuecity varchar(30),
	venuestate char(2),
	venueseats integer);

create table category(
	catid smallint not null distkey sortkey,
	catgroup varchar(10),
	catname varchar(10),
	catdesc varchar(50));

create table date(
	dateid smallint not null distkey sortkey,
	caldate date not null,
	day character(3) not null,
	week smallint not null,
	month character(5) not null,
	qtr character(5) not null,
	year smallint not null,
	holiday boolean default('N'));

create table event(
	eventid integer not null distkey,
	venueid smallint not null,
	catid smallint not null,
	dateid smallint not null sortkey,
	eventname varchar(200),
	starttime timestamp);

create table listing(
	listid integer not null distkey,
	sellerid integer not null,
	eventid integer not null,
	dateid smallint not null  sortkey,
	numtickets smallint not null,
	priceperticket decimal(8,2),
	totalprice decimal(8,2),
	listtime timestamp);

create table sales(
	salesid integer not null,
	listid integer not null distkey,
	sellerid integer not null,
	buyerid integer not null,
	eventid integer not null,
	dateid smallint not null sortkey,
	qtysold smallint not null,
	pricepaid decimal(8,2),
	commission decimal(8,2),
	saletime timestamp);
	
It ran quickly

I ran this command:

copy users from 's3://awssampledbuswest2/tickit/allusers_pipe.txt' 
credentials 'aws_iam_role=arn:aws:iam::448496253599:role/myRedshiftRole'
delimiter '|' region 'us-west-2';

I saw this:

Warnings:
Load into table 'users' completed, 49990 record(s) loaded successfully.

0 rows affected
COPY executed successfully

Execution time: 50.36s


I ran more commands:


copy venue from 's3://awssampledbuswest2/tickit/venue_pipe.txt' 
credentials 'aws_iam_role=arn:aws:iam::448496253599:role/myRedshiftRole'
delimiter '|' region 'us-west-2';

copy category from 's3://awssampledbuswest2/tickit/category_pipe.txt' 
credentials 'aws_iam_role=arn:aws:iam::448496253599:role/myRedshiftRole'
delimiter '|' region 'us-west-2';

copy date from 's3://awssampledbuswest2/tickit/date2008_pipe.txt' 
credentials 'aws_iam_role=arn:aws:iam::448496253599:role/myRedshiftRole'
delimiter '|' region 'us-west-2';

copy event from 's3://awssampledbuswest2/tickit/allevents_pipe.txt' 
credentials 'aws_iam_role=arn:aws:iam::448496253599:role/myRedshiftRole'
delimiter '|' timeformat 'YYYY-MM-DD HH:MI:SS' region 'us-west-2';

copy listing from 's3://awssampledbuswest2/tickit/listings_pipe.txt' 
credentials 'aws_iam_role=arn:aws:iam::448496253599:role/myRedshiftRole'
delimiter '|' region 'us-west-2';

copy sales from 's3://awssampledbuswest2/tickit/sales_tab.txt'
credentials 'aws_iam_role=arn:aws:iam::448496253599:role/myRedshiftRole'
delimiter '\t' timeformat 'MM/DD/YYYY HH:MI:SS' region 'us-west-2';


I saw this:

Warnings:
Load into table 'venue' completed, 202 record(s) loaded successfully.

0 rows affected
COPY executed successfully

Execution time: 20.84s
Statement 1 of 6 finished

Warnings:
Load into table 'category' completed, 11 record(s) loaded successfully.

0 rows affected
COPY executed successfully

Execution time: 17.87s
Statement 2 of 6 finished

Warnings:
Load into table 'date' completed, 365 record(s) loaded successfully.

0 rows affected
COPY executed successfully

Execution time: 24.79s
Statement 3 of 6 finished

Warnings:
Load into table 'event' completed, 8798 record(s) loaded successfully.

0 rows affected
COPY executed successfully

Execution time: 21.25s
Statement 4 of 6 finished

Warnings:
Load into table 'listing' completed, 192497 record(s) loaded successfully.

0 rows affected
COPY executed successfully

Execution time: 26.03s
Statement 5 of 6 finished



I queried the data with SELECT statements:

-- Get definition for the sales table.
SELECT *    
FROM pg_table_def    
WHERE tablename = 'sales';    

-- Find total sales on a given calendar date.
SELECT sum(qtysold) 
FROM   sales, date 
WHERE  sales.dateid = date.dateid 
AND    caldate = '2008-01-05';

-- Find top 10 buyers by quantity.
SELECT firstname, lastname, total_quantity 
FROM   (SELECT buyerid, sum(qtysold) total_quantity
        FROM  sales
        GROUP BY buyerid
        ORDER BY total_quantity desc limit 10) Q, users
WHERE Q.buyerid = userid
ORDER BY Q.total_quantity desc;

-- Find events in the 99.9 percentile in terms of all time gross sales.
SELECT eventname, total_price 
FROM  (SELECT eventid, total_price, ntile(1000) over(order by total_price desc) as percentile 
       FROM (SELECT eventid, sum(pricepaid) total_price
             FROM   sales
             GROUP BY eventid)) Q, event E
       WHERE Q.eventid = E.eventid
       AND percentile = 1
ORDER BY total_price desc;


All four statements ran and returned interesting results.



I visited this URL:

https://console.aws.amazon.com/redshift/

I clicked the link to my cluster: redshift-cluster-1

I clicked the Queries tab.

I saw a page full of information about my activity.

I picked this query:

-- Find top 10 buyers by quantity. SELECT firstname, lastname,
   total_quantity FROM (SELECT buyerid, sum(qtysold) total_quantity
   FROM sales GROUP BY buyerid ORDER BY total_quantity desc limit 10)
   Q, users WHERE Q.buyerid = userid ORDER BY Q.total_quantity desc

I saw that it ran in 10.47s

Also it showed me a query-plan:

XN Merge (cost=2000001005556.17..2000001005556.19 rows=10 width=27)
    -> XN Network (cost=2000001005556.17..2000001005556.19 rows=10 width=27)
      -> XN Sort (cost=2000001005556.17..2000001005556.19 rows=10 width=27)
        -> XN Hash Join DS_DIST_INNER (cost=1000000004431.13..1000001005556.00 rows=10 width=27)
          -> XN Seq Scan on users (cost=0.00..499.90 rows=49990 width=23)
          -> XN Hash (cost=1000000004431.10..1000000004431.10 rows=10 width=12)
            -> XN Subquery Scan q (cost=1000000004430.98..1000000004431.10 rows=10 width=12)
              -> XN Limit (cost=1000000004430.98..1000000004431.00 rows=10 width=6)
  -> XN HashAggregate (cost=2586.84..2647.99 rows=24461 width=6)
    -> XN Seq Scan on sales (cost=0.00..1724.56 rows=172456 width=6)

And it showed time-series plots of measurements:
  cpu, i/o, network, ...

I was done so I wanted to shutdown the cluster to prevent charges.

Next I revoked Access from the VPC Security Group

I visited 

https://us-west-2.console.aws.amazon.com/redshift
I choose Clusters.
clicked redshift-cluster-1

I should land in Configuration tab.

Find my security group

I saw this link:

VPC security groupsList of VPC Security Groups associated with this cluster.	
default (sg-b0e2acc3)
 ( active )

I removed the rule with description: redshift5439

I visited 

https://us-west-2.console.aws.amazon.com/redshift
I choose Clusters.
clicked redshift-cluster-1

I found the delete link and clicked it.

Eventually AWS deleted the cluster and stopped charging me money.


