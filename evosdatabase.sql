PGDMP     *    3                y            evosdatabase    13.2    13.2 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    41020    evosdatabase    DATABASE     v   CREATE DATABASE evosdatabase WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Uzbek (Cyrillic)_Uzbekistan.1251';
    DROP DATABASE evosdatabase;
                postgres    false            �            1259    49212    buylist    TABLE     �   CREATE TABLE public.buylist (
    id integer,
    product_name character varying(255),
    date character varying(255),
    count integer
);
    DROP TABLE public.buylist;
       public         heap    postgres    false            �            1259    41053    category    TABLE     t   CREATE TABLE public.category (
    id integer,
    category_name character varying(255),
    category_id integer
);
    DROP TABLE public.category;
       public         heap    postgres    false            �            1259    41021    products    TABLE     �   CREATE TABLE public.products (
    product_id integer,
    product_name character varying(255),
    category_id integer,
    price integer
);
    DROP TABLE public.products;
       public         heap    postgres    false            �          0    49212    buylist 
   TABLE DATA           @   COPY public.buylist (id, product_name, date, count) FROM stdin;
    public          postgres    false    202   .	       �          0    41053    category 
   TABLE DATA           B   COPY public.category (id, category_name, category_id) FROM stdin;
    public          postgres    false    201   �
       �          0    41021    products 
   TABLE DATA           P   COPY public.products (product_id, product_name, category_id, price) FROM stdin;
    public          postgres    false    200   �
       �   J  x���MV�0�5�"��$3��� nh�Q|�P>|���7Y�^2�h�E'�����֖i A�xJHi�+���Е�����}*rQg�}�
DZ��6-�n��2}O���(�46��Vb���#`�|���N꛴�Hb�PB���i��a�LL�8QA���YՉ<=��&�G�t�����o�v�Q�O't� ��}i��(B��lշ��d�t��a��Y�^B.(n�2���_��/Ԇ���:X�B5�u�E�4��aΙ���|�x�KR����]����7YH4�۝����%#?��Z ��������$l      �   Q   x�3��I,K,��I,�4�2��,.�,T�L�������qs'�f�s�pdVU%r�p�r��g�er�r��qqq ���      �     x�M��R�0���S�`t����PQPR�(��v�`����ɉ�r����I���9��1�Ad�M�Bd��u,5K�o?����$$��ܯD@������:'k�uV'Ԛ�a�Z;1Wܺ��N~�-,x���7�i���	��1�N6��n��-z��D�Y춞�7R����[&�F�HN�J}e�o[���
gw�P*�h�����B��D;�8���\W��>��b�]�S�����P�>A"t�_r��ղX\I��?`�fe�`�
���,���+�!     