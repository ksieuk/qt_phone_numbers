--
-- PostgreSQL database dump
--

-- Dumped from database version 10.22
-- Dumped by pg_dump version 13.1

-- Started on 2022-12-09 09:00:34

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

SET default_tablespace = '';

--
-- TOC entry 197 (class 1259 OID 16404)
-- Name: surname; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surname (
    surname_id integer NOT NULL,
    surname_value character(30) NOT NULL
);


ALTER TABLE public.surname OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16402)
-- Name: surname_surname_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.surname_surname_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.surname_surname_id_seq OWNER TO postgres;

--
-- TOC entry 2849 (class 0 OID 0)
-- Dependencies: 196
-- Name: surname_surname_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.surname_surname_id_seq OWNED BY public.surname.surname_id;


--
-- TOC entry 199 (class 1259 OID 16428)
-- Name: name; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.first_name (
    first_name_id integer NOT NULL,
    first_name_value character(35) NOT NULL
);


ALTER TABLE public.first_name OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16426)
-- Name: name_first_name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.first_name_first_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.first_name_first_name_id_seq OWNER TO postgres;

--
-- TOC entry 2850 (class 0 OID 0)
-- Dependencies: 198
-- Name: name_first_name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.first_name_first_name_id_seq OWNED BY public.first_name.first_name_id;


--
-- TOC entry 201 (class 1259 OID 16436)
-- Name: middle_name; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.middle_name (
    middle_name_id integer NOT NULL,
    middle_name_value character(35) NOT NULL
);


ALTER TABLE public.middle_name OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16434)
-- Name: middle_name_middle_name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.middle_name_middle_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.middle_name_middle_name_id_seq OWNER TO postgres;

--
-- TOC entry 2851 (class 0 OID 0)
-- Dependencies: 200
-- Name: middle_name_middle_name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.middle_name_middle_name_id_seq OWNED BY public.middle_name.middle_name_id;


--
-- TOC entry 205 (class 1259 OID 16452)
-- Name: street; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.street (
    street_id integer NOT NULL,
    street_value character(35) NOT NULL
);


ALTER TABLE public.street OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16450)
-- Name: street_street_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.street_street_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.street_street_id_seq OWNER TO postgres;

--
-- TOC entry 2852 (class 0 OID 0)
-- Dependencies: 204
-- Name: street_street_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.street_street_id_seq OWNED BY public.street.street_id;


--
-- TOC entry 203 (class 1259 OID 16444)
-- Name: phone_number_baza; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.phone_number_baza (
    uniq_id integer NOT NULL,
    surname integer NOT NULL,
    first_name integer NOT NULL,
    middle_name integer,
    street integer NOT NULL,
    house character(5) NOT NULL,
    building character(5),
    apartment character(5) NOT NULL,
    phone_number character(35) NOT NULL
);


ALTER TABLE public.phone_number_baza OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16442)
-- Name: phone_number_baza_uniq_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.phone_number_baza_uniq_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.phone_number_baza_uniq_id_seq OWNER TO postgres;

--
-- TOC entry 2853 (class 0 OID 0)
-- Dependencies: 202
-- Name: phone_number_baza_uniq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.phone_number_baza_uniq_id_seq OWNED BY public.phone_number_baza.uniq_id;


--
-- TOC entry 2694 (class 2604 OID 16407)
-- Name: surname surname_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surname ALTER COLUMN surname_id SET DEFAULT nextval('public.surname_surname_id_seq'::regclass);


--
-- TOC entry 2695 (class 2604 OID 16431)
-- Name: name first_name_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.first_name ALTER COLUMN first_name_id SET DEFAULT nextval('public.first_name_first_name_id_seq'::regclass);


--
-- TOC entry 2696 (class 2604 OID 16439)
-- Name: middle_name middle_name_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.middle_name ALTER COLUMN middle_name_id SET DEFAULT nextval('public.middle_name_middle_name_id_seq'::regclass);


--
-- TOC entry 2698 (class 2604 OID 16455)
-- Name: street street_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.street ALTER COLUMN street_id SET DEFAULT nextval('public.street_street_id_seq'::regclass);


--
-- TOC entry 2697 (class 2604 OID 16447)
-- Name: phone_number_baza uniq_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_number_baza ALTER COLUMN uniq_id SET DEFAULT nextval('public.phone_number_baza_uniq_id_seq'::regclass);


--
-- TOC entry 2835 (class 0 OID 16404)
-- Dependencies: 197
-- Data for Name: surname; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.surname (surname_id, surname_value) VALUES (1, 'Иванов');
INSERT INTO public.surname (surname_id, surname_value) VALUES (2, 'Вестяк');
INSERT INTO public.surname (surname_id, surname_value) VALUES (3, 'Давыдов');
INSERT INTO public.surname (surname_id, surname_value) VALUES (4, 'Прокофьев');
INSERT INTO public.surname (surname_id, surname_value) VALUES (5, 'Сухарев');
INSERT INTO public.surname (surname_id, surname_value) VALUES (6, 'Бугулов');
INSERT INTO public.surname (surname_id, surname_value) VALUES (7, 'Миролюбов');
INSERT INTO public.surname (surname_id, surname_value) VALUES (8, 'Топорков');
INSERT INTO public.surname (surname_id, surname_value) VALUES (9, 'Алешкин');
INSERT INTO public.surname (surname_id, surname_value) VALUES (10, 'Смирнов');
INSERT INTO public.surname (surname_id, surname_value) VALUES (11, 'Петров');
INSERT INTO public.surname (surname_id, surname_value) VALUES (12, 'Ласточкин');
INSERT INTO public.surname (surname_id, surname_value) VALUES (13, 'Григорьев');
INSERT INTO public.surname (surname_id, surname_value) VALUES (14, 'Ололоев');
INSERT INTO public.surname (surname_id, surname_value) VALUES (15, 'Мирный');




--
-- TOC entry 2837 (class 0 OID 16428)
-- Dependencies: 199
-- Data for Name: name; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (1, 'Иван');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (2, 'Владимир');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (3, 'Анатолий');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (4, 'Сергей');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (5, 'Александр');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (6, 'Богдан');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (7, 'Максим');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (8, 'Алексей');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (9, 'Николай');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (10, 'Назар');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (11, 'Андрей');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (12, 'Тагир');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (13, 'Ахмедхан');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (14, 'Святослав');
INSERT INTO public.first_name (first_name_id, first_name_value) VALUES (15, 'Ярослав');




--
-- TOC entry 2839 (class 0 OID 16436)
-- Dependencies: 201
-- Data for Name: middle_name; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (1, 'Алексеевич');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (2, 'Александрович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (3, 'Сергеевич');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (4, 'Анатольевич');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (5, 'Владимирович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (6, 'Максимович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (7, 'Игоревич');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (8, 'Тимурович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (9, 'Владиславович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (10, 'Асланбекович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (11, 'Саидович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (12, 'Маратович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (13, 'Олегович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (14, 'Глебович');
INSERT INTO public.middle_name (middle_name_id, middle_name_value) VALUES (15, 'Ильич');



--
-- TOC entry 2843 (class 0 OID 16452)
-- Dependencies: 205
-- Data for Name: street; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.street (street_id, street_value) VALUES (1, 'Армавирская');
INSERT INTO public.street (street_id, street_value) VALUES (2, 'Мусы Джалиля');
INSERT INTO public.street (street_id, street_value) VALUES (3, 'Арбат');
INSERT INTO public.street (street_id, street_value) VALUES (4, '40 лет октября');
INSERT INTO public.street (street_id, street_value) VALUES (5, 'Краснодарская');
INSERT INTO public.street (street_id, street_value) VALUES (6, 'Краснодонская');
INSERT INTO public.street (street_id, street_value) VALUES (7, 'Таганрогская');
INSERT INTO public.street (street_id, street_value) VALUES (8, 'Краснопёрская');
INSERT INTO public.street (street_id, street_value) VALUES (9, 'Дубосековская');
INSERT INTO public.street (street_id, street_value) VALUES (10, 'Лескова');
INSERT INTO public.street (street_id, street_value) VALUES (11, 'Люблинская');
INSERT INTO public.street (street_id, street_value) VALUES (12, 'Большая Академическая');
INSERT INTO public.street (street_id, street_value) VALUES (13, 'Тверская');
INSERT INTO public.street (street_id, street_value) VALUES (14, 'Лубянка');
INSERT INTO public.street (street_id, street_value) VALUES (15, 'Гоголевский бульвар');




--
-- TOC entry 2841 (class 0 OID 16444)
-- Dependencies: 203
-- Data for Name: phone_number_baza; Type: TABLE DATA; Schema: public; Owner: postgres
--

-- INSERT INTO public.phone_number_baza (uniq_id, surname, name, middle_name, street, house, building, apartment, phone_number) VALUES (1, 1, 1, 1, 1, '5    ', '2    ', '7    ', '88005553535                        ');
-- INSERT INTO public.phone_number_baza (uniq_id, surname, name, middle_name, street, house, building, apartment, phone_number) VALUES (2, 2, 1, 3, 1, '3    ', '1    ', '37   ', '89660029099                        ');


--
-- TOC entry 2854 (class 0 OID 0)
-- Dependencies: 196
-- Name: surname_surname_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.surname_surname_id_seq', 15, true);


--
-- TOC entry 2855 (class 0 OID 0)
-- Dependencies: 198
-- Name: name_first_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.first_name_first_name_id_seq', 15, true);


--
-- TOC entry 2856 (class 0 OID 0)
-- Dependencies: 200
-- Name: middle_name_middle_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.middle_name_middle_name_id_seq', 15, true);


--
-- TOC entry 2857 (class 0 OID 0)
-- Dependencies: 204
-- Name: street_street_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.street_street_id_seq', 15, true);


--
-- TOC entry 2858 (class 0 OID 0)
-- Dependencies: 202
-- Name: phone_number_baza_uniq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.phone_number_baza_uniq_id_seq', 1, true);


--
-- TOC entry 2700 (class 2606 OID 16409)
-- Name: surname surname_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surname
    ADD CONSTRAINT surname_pkey PRIMARY KEY (surname_id);


--
-- TOC entry 2702 (class 2606 OID 16433)
-- Name: name name_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.first_name
    ADD CONSTRAINT name_pkey PRIMARY KEY (first_name_id);


--
-- TOC entry 2704 (class 2606 OID 16441)
-- Name: middle_name middle_name_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.middle_name
    ADD CONSTRAINT middle_name_pkey PRIMARY KEY (middle_name_id);


--
-- TOC entry 2708 (class 2606 OID 16457)
-- Name: street street_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.street
    ADD CONSTRAINT street_pkey PRIMARY KEY (street_id);


--
-- TOC entry 2706 (class 2606 OID 16449)
-- Name: phone_number_baza phone_number_baza_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_number_baza
    ADD CONSTRAINT phone_number_baza_pkey PRIMARY KEY (uniq_id);


--
-- TOC entry 2709 (class 2606 OID 16458)
-- Name: phone_number_baza fk_surname; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_number_baza
    ADD CONSTRAINT fk_surname FOREIGN KEY (surname) REFERENCES public.surname(surname_id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


--
-- TOC entry 2710 (class 2606 OID 16463)
-- Name: phone_number_baza fk_name; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_number_baza
    ADD CONSTRAINT fk_name FOREIGN KEY (first_name) REFERENCES public.first_name(first_name_id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


--
-- TOC entry 2711 (class 2606 OID 16468)
-- Name: phone_number_baza fk_middle_name; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_number_baza
    ADD CONSTRAINT fk_middle_name FOREIGN KEY (middle_name) REFERENCES public.middle_name(middle_name_id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


--
-- TOC entry 2712 (class 2606 OID 16473)
-- Name: phone_number_baza fk_street; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_number_baza
    ADD CONSTRAINT fk_street FOREIGN KEY (street) REFERENCES public.street(street_id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


-- Completed on 2022-12-09 09:00:34

--
-- PostgreSQL database dump complete
--

