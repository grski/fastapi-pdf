SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: chat; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.chat (
    uuid character varying(255),
    user_uuid character varying(255),
    is_active boolean,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    input_message_id integer NOT NULL,
    output_message_id integer NOT NULL
);


--
-- Name: inputmessage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.inputmessage (
    id integer NOT NULL,
    user_uuid character varying(255),
    role character varying(255),
    input_text text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);


--
-- Name: inputmessage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.inputmessage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: inputmessage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.inputmessage_id_seq OWNED BY public.inputmessage.id;


--
-- Name: invitation_keys; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invitation_keys (
    id integer NOT NULL,
    uuid character varying(255) NOT NULL,
    is_used boolean NOT NULL,
    user_email character varying(255) NOT NULL,
    message_limit integer NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);


--
-- Name: invitation_keys_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.invitation_keys_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: invitation_keys_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.invitation_keys_id_seq OWNED BY public.invitation_keys.id;


--
-- Name: outputmessage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.outputmessage (
    id integer NOT NULL,
    user_uuid character varying(255),
    output_text text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);


--
-- Name: outputmessage_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.outputmessage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: outputmessage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.outputmessage_id_seq OWNED BY public.outputmessage.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.schema_migrations (
    version character varying(128) NOT NULL
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(255),
    email character varying(255),
    is_confirmed boolean,
    uuid character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: inputmessage id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.inputmessage ALTER COLUMN id SET DEFAULT nextval('public.inputmessage_id_seq'::regclass);


--
-- Name: invitation_keys id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invitation_keys ALTER COLUMN id SET DEFAULT nextval('public.invitation_keys_id_seq'::regclass);


--
-- Name: outputmessage id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.outputmessage ALTER COLUMN id SET DEFAULT nextval('public.outputmessage_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: chat chat_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (input_message_id, output_message_id);


--
-- Name: inputmessage inputmessage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.inputmessage
    ADD CONSTRAINT inputmessage_pkey PRIMARY KEY (id);


--
-- Name: invitation_keys invitation_keys_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invitation_keys
    ADD CONSTRAINT invitation_keys_pkey PRIMARY KEY (id);


--
-- Name: invitation_keys invitation_keys_user_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invitation_keys
    ADD CONSTRAINT invitation_keys_user_email_key UNIQUE (user_email);


--
-- Name: invitation_keys invitation_keys_uuid_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invitation_keys
    ADD CONSTRAINT invitation_keys_uuid_key UNIQUE (uuid);


--
-- Name: outputmessage outputmessage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.outputmessage
    ADD CONSTRAINT outputmessage_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_uuid_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_uuid_key UNIQUE (uuid);


--
-- Name: chat chat_input_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT chat_input_message_id_fkey FOREIGN KEY (input_message_id) REFERENCES public.inputmessage(id);


--
-- Name: chat chat_output_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT chat_output_message_id_fkey FOREIGN KEY (output_message_id) REFERENCES public.outputmessage(id);


--
-- PostgreSQL database dump complete
--


--
-- Dbmate schema migrations
--

INSERT INTO public.schema_migrations (version) VALUES
    ('20230925090948');
