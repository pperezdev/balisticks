------------------------------------------------------------
--        Script Postgre 
------------------------------------------------------------



------------------------------------------------------------
-- Table: USERS
------------------------------------------------------------
CREATE TABLE public.USERS(
	id                SERIAL NOT NULL ,
	pseudo            VARCHAR (50) NOT NULL ,
	name              VARCHAR (50) NOT NULL ,
	surname           VARCHAR (50) NOT NULL ,
	mail              VARCHAR (50) NOT NULL ,
	password          VARCHAR (50) NOT NULL ,
	phone             VARCHAR (10) NOT NULL ,
	birthday          DATE  NOT NULL ,
	picture           VARCHAR (10) NOT NULL ,
	banner            VARCHAR (10) NOT NULL ,
	inscriptiondate   DATE  NOT NULL  ,
	CONSTRAINT USERS_PK PRIMARY KEY (id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: ORGANISATIONS
------------------------------------------------------------
CREATE TABLE public.ORGANISATIONS(
	id                SERIAL NOT NULL  ,
	name              VARCHAR (50) NOT NULL ,
	picture           VARCHAR (10) NOT NULL ,
	banner            VARCHAR (10) NOT NULL ,
	creationdate      DATE  NOT NULL  ,
	CONSTRAINT ORGANISATIONS_PK PRIMARY KEY (id)
)WITHOUT OIDS;

------------------------------------------------------------
-- Table: ORGANISATIONSUSERS
------------------------------------------------------------
CREATE TABLE public.ORGANISATIONSUSERS(
	id                 SERIAL NOT NULL ,
	id_ORGANISATIONS   INT  NOT NULL ,
	id_USERS           INT  NOT NULL  ,
	CONSTRAINT ORGANISATIONSUSERS_PK PRIMARY KEY (id)

	,CONSTRAINT ORGANISATIONSUSERS_ORGANISATIONS_FK FOREIGN KEY (id_ORGANISATIONS) REFERENCES public.ORGANISATIONS(id)
	,CONSTRAINT ORGANISATIONSUSERS_USERS0_FK FOREIGN KEY (id_USERS) REFERENCES public.USERS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: PROPERTIES
------------------------------------------------------------
CREATE TABLE public.PROPERTIES(
	id     SERIAL NOT NULL ,
	name   VARCHAR (50) NOT NULL  ,
	CONSTRAINT PROPERTIES_PK PRIMARY KEY (id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: CHECKLISTS
------------------------------------------------------------
CREATE TABLE public.CHECKLISTS(
	id     INT  NOT NULL ,
	name   VARCHAR (50) NOT NULL  ,
	CONSTRAINT CHECKLISTS_PK PRIMARY KEY (id)

	,CONSTRAINT CHECKLISTS_PROPERTIES_FK FOREIGN KEY (id) REFERENCES public.PROPERTIES(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: TEXTS
------------------------------------------------------------
CREATE TABLE public.TEXTS(
	id        INT  NOT NULL ,
	Content   VARCHAR (50) NOT NULL ,
	name      VARCHAR (50) NOT NULL  ,
	CONSTRAINT TEXTS_PK PRIMARY KEY (id)

	,CONSTRAINT TEXTS_PROPERTIES_FK FOREIGN KEY (id) REFERENCES public.PROPERTIES(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: DATETYPES
------------------------------------------------------------
CREATE TABLE public.DATETYPES(
	id        SERIAL NOT NULL ,
	libelle   VARCHAR (50) NOT NULL  ,
	CONSTRAINT DATETYPES_PK PRIMARY KEY (id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: DATES
------------------------------------------------------------
CREATE TABLE public.DATES(
	id             INT  NOT NULL ,
	date           DATE  NOT NULL ,
	name           VARCHAR (50) NOT NULL ,
	id_DATETYPES   INT  NOT NULL  ,
	CONSTRAINT DATES_PK PRIMARY KEY (id)

	,CONSTRAINT DATES_PROPERTIES_FK FOREIGN KEY (id) REFERENCES public.PROPERTIES(id)
	,CONSTRAINT DATES_DATETYPES0_FK FOREIGN KEY (id_DATETYPES) REFERENCES public.DATETYPES(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: TIMES
------------------------------------------------------------
CREATE TABLE public.TIMES(
	id        INT  NOT NULL ,
	libelle   VARCHAR (50) NOT NULL ,
	name      VARCHAR (50) NOT NULL  ,
	CONSTRAINT TIMES_PK PRIMARY KEY (id)

	,CONSTRAINT TIMES_PROPERTIES_FK FOREIGN KEY (id) REFERENCES public.PROPERTIES(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: CHECKS
------------------------------------------------------------
CREATE TABLE public.CHECKS(
	id              SERIAL NOT NULL ,
	libelle         VARCHAR (50) NOT NULL ,
	isCheck         BOOL  NOT NULL ,
	id_CHECKLISTS   INT  NOT NULL  ,
	CONSTRAINT CHECKS_PK PRIMARY KEY (id)

	,CONSTRAINT CHECKS_CHECKLISTS_FK FOREIGN KEY (id_CHECKLISTS) REFERENCES public.CHECKLISTS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: USERSTYPE 
------------------------------------------------------------
CREATE TABLE public.USERSTYPE(
	id        SERIAL NOT NULL ,
	libelle   VARCHAR (50) NOT NULL  ,
	CONSTRAINT USERSTYPE_PK PRIMARY KEY (id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: PROJECTS
------------------------------------------------------------
CREATE TABLE public.PROJECTS(
	id                 SERIAL NOT NULL ,
	libelle            VARCHAR (50) NOT NULL ,
	description        VARCHAR (50) NOT NULL ,
	picture            VARCHAR (50) NOT NULL ,
	banner             VARCHAR (50) NOT NULL ,
	id_ORGANISATIONS   INT   ,
	id_USERS           INT  NOT NULL  ,
	CONSTRAINT PROJECTS_PK PRIMARY KEY (id)

	,CONSTRAINT PROJECTS_ORGANISATIONS_FK FOREIGN KEY (id_ORGANISATIONS) REFERENCES public.ORGANISATIONS(id)
	,CONSTRAINT PROJECTS_USERS0_FK FOREIGN KEY (id_USERS) REFERENCES public.USERS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: WORKSPACES
------------------------------------------------------------
CREATE TABLE public.WORKSPACES(
	id            SERIAL NOT NULL ,
	libelle       VARCHAR (50) NOT NULL ,
	id_PROJECTS   INT    ,
	CONSTRAINT WORKSPACES_PK PRIMARY KEY (id)

	,CONSTRAINT WORKSPACES_PROJECTS_FK FOREIGN KEY (id_PROJECTS) REFERENCES public.PROJECTS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: TASKS
------------------------------------------------------------
CREATE TABLE public.TASKS(
	id              SERIAL NOT NULL ,
	libelle         VARCHAR (50) NOT NULL ,
	createddate     DATE  NOT NULL ,
	id_WORKSPACES   INT   ,
	id_PROJECTS     INT  NOT NULL  ,
	CONSTRAINT TASKS_PK PRIMARY KEY (id)

	,CONSTRAINT TASKS_WORKSPACES_FK FOREIGN KEY (id_WORKSPACES) REFERENCES public.WORKSPACES(id)
	,CONSTRAINT TASKS_PROJECTS0_FK FOREIGN KEY (id_PROJECTS) REFERENCES public.PROJECTS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: TASKSPROPERTIES
------------------------------------------------------------
CREATE TABLE public.TASKSPROPERTIES(
	id              SERIAL NOT NULL ,
	id_PROPERTIES   INT  NOT NULL ,
	id_TASKS        INT  NOT NULL  ,
	CONSTRAINT TASKSPROPERTIES_PK PRIMARY KEY (id)

	,CONSTRAINT TASKSPROPERTIES_PROPERTIES_FK FOREIGN KEY (id_PROPERTIES) REFERENCES public.PROPERTIES(id)
	,CONSTRAINT TASKSPROPERTIES_TASKS0_FK FOREIGN KEY (id_TASKS) REFERENCES public.TASKS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: USERSTASKS
------------------------------------------------------------
CREATE TABLE public.USERSTASKS(
	id              SERIAL NOT NULL ,
	id_USERSTYPE    INT  NOT NULL ,
	id_TASKS        INT  NOT NULL ,
	id_USERS        INT  NOT NULL  ,
	CONSTRAINT USERSTASKS_PK PRIMARY KEY (id)

	,CONSTRAINT USERSTASKS_USERSTYPE_FK FOREIGN KEY (id_USERSTYPE) REFERENCES public.USERSTYPE(id)
	,CONSTRAINT USERSTASKS_TASKS0_FK FOREIGN KEY (id_TASKS) REFERENCES public.TASKS(id)
	,CONSTRAINT USERSTASKS_USERS1_FK FOREIGN KEY (id_USERS) REFERENCES public.USERS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: PROJECTSUSERS
------------------------------------------------------------
CREATE TABLE public.PROJECTSUSERS(
	id            SERIAL NOT NULL ,
	id_USERS      INT  NOT NULL ,
	id_PROJECTS   INT  NOT NULL  ,
	CONSTRAINT PROJECTSUSERS_PK PRIMARY KEY (id)

	,CONSTRAINT PROJECTSUSERS_USERS_FK FOREIGN KEY (id_USERS) REFERENCES public.USERS(id)
	,CONSTRAINT PROJECTSUSERS_PROJECTS0_FK FOREIGN KEY (id_PROJECTS) REFERENCES public.PROJECTS(id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: TAGTYPE
------------------------------------------------------------
CREATE TABLE public.TAGTYPE(
	id        SERIAL NOT NULL ,
	libelle   VARCHAR (50) NOT NULL  ,
	CONSTRAINT TAGTYPE_PK PRIMARY KEY (id)
)WITHOUT OIDS;


------------------------------------------------------------
-- Table: TAGS
------------------------------------------------------------
CREATE TABLE public.TAGS(
	id           INT  NOT NULL ,
	name         VARCHAR (50) NOT NULL ,
	id_TAGTYPE   INT  NOT NULL  ,
	CONSTRAINT TAGS_PK PRIMARY KEY (id)

	,CONSTRAINT TAGS_PROPERTIES_FK FOREIGN KEY (id) REFERENCES public.PROPERTIES(id)
	,CONSTRAINT TAGS_TAGTYPE0_FK FOREIGN KEY (id_TAGTYPE) REFERENCES public.TAGTYPE(id)
)WITHOUT OIDS;