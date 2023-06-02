--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Debian 12.4-1.pgdg100+1)
-- Dumped by pg_dump version 12.4 (Debian 12.4-1.pgdg100+1)

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

SET default_table_access_method = heap;

CREATE DATABASE data;

--
-- Name: br_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.br_data (
    br_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    br_timepoint character varying(50),
    br_data_entry_dt date,
    br_btf_who character varying(150),
    br_btf_hereditary character varying(50),
    br_btf_menopause character varying(100),
    br_btf_tum_loc character varying(50),
    br_btf_lateraltiy character varying(50),
    br_btf_tnmedition character varying(50),
    br_btf_ctstage character varying(50),
    br_btf_cnstage character varying(50),
    br_btf_cmstage character varying(50),
    br_dpr_diag_mri character varying(50),
    br_dpr_diag_bonesc character varying(50),
    br_dpr_diag_ct character varying(50),
    br_dpr_diag_petct character varying(50),
    br_dpr_ax_punct character varying(50),
    br_dpr_concl_ax_punct character varying(50),
    br_dpr_ln_mapping character varying(50),
    br_dpr_timing_snproc_other character varying(50),
    br_dpr_concl_lnmap character varying(100),
    br_dpr_nodes_resec_diag integer,
    br_dpr_nodes_involv_diag integer,
    br_dpr_exgrowth_ln character varying(50),
    br_dpr_parast_drain character varying(50),
    br_dpr_diast_bp character varying(50),
    br_dpr_syst_bp character varying(50),
    br_dpr_hba1c character varying(50),
    br_dpr_ldl_chol character varying(50),
    br_dpr_tot_chol character varying(50),
    br_dpr_triglycerides character varying(50),
    br_dpr_hscrp character varying(50),
    br_dpr_tsh character varying(50),
    br_dpr_ft4 character varying(50),
    br_pr_date_diag character varying(50),
    br_pr_invasive character varying(50),
    br_pr_inv_histo character varying(50),
    br_pr_inv_histo_other character varying(50),
    br_pr_multifocality character varying(50),
    br_pr_inv_size character varying(50),
    br_pr_inv_grade_diff character varying(50),
    br_pr_min_res_marg_inv character varying(50),
    br_pr_lymphang_inv character varying(50),
    br_pr_progestrone character varying(50),
    br_pr_oestrogen character varying(50),
    br_pr_her2 character varying(50),
    br_pr_ki67_test character varying(50),
    br_pr_ki67_value character varying(50),
    br_pr_molec_prof character varying(50),
    br_pr_insitu character varying(50),
    br_pr_situ_histo character varying(50),
    br_pr_situ_histo_other character varying(50),
    br_pr_size_dcis character varying(50),
    br_pr_ext_dcis character varying(50),
    br_pr_situ_grade_diff character varying(50),
    br_pr_res_marg_situ character varying(50),
    br_pr_ptstage character varying(50),
    br_pr_yptstage character varying(50),
    br_pr_pnstage character varying(50),
    br_pr_ypnstage character varying(50),
    br_sp_date_surg date,
    br_sp_type_surg character varying(50),
    br_sp_plastic_surg character varying(50),
    br_sp_re_resec character varying(50),
    br_sp_re_resec_date date,
    br_sp_tum_stat_reresec character varying(50),
    br_sp_postop_hematoma character varying(50),
    br_sp_postop_seroma character varying(50),
    br_sp_postop_infect character varying(50),
    br_sp_ax_ln_dissect character varying(50),
    br_sp_ax_ln_dissect_date date,
    br_sp_nodes_resec integer,
    br_sp_nodes_involv integer,
    br_sp_size_largest_ln character varying(50),
    br_sp_extran_growth character varying(50),
    br_sp_number_extrangr character varying(50),
    br_sp_topnode_pos character varying(50),
    br_sp_intrabr_bl_ln character varying(50),
    br_sp_intrabr_bl_ln_res character varying(50),
    br_sp_invol_intrabr_bl_ln character varying(50),
    br_caost_chemo character varying(50),
    br_caost_chemo_start_date date,
    br_caost_chemo_last_date date,
    br_caost_chemo_fec_cef character varying(50),
    br_caost_chemo_cycles_feccef integer,
    br_caost_chemo_ac character varying(50),
    br_caost_chemo_cycles_ac integer,
    br_caost_chemo_cmf character varying(50),
    br_caost_chemo_cycles_cmf integer,
    br_caost_chemo_doce_taxo character varying(50),
    br_caost_chemo_cycles_docetaxo integer,
    br_caost_chemo_pacl_taxol character varying(50),
    br_caost_chemo_cycles_pacltax integer,
    br_caost_ht character varying(50),
    br_caost_ht_start_date date,
    br_caost_ht_duration character varying(50),
    br_caost_tamoxifen character varying(50),
    br_caost_arom_inhb character varying(50),
    br_caost_ht_other character varying(50),
    br_caost_targeted character varying(50),
    br_caost_targeted_name character varying(100),
    br_caost_target_start_date date,
    br_caost_target_stop_date date,
    br_rrf_rt_rob_plan character varying(50),
    br_rrf_rt_rob_op_trans_x character varying(50),
    br_rrf_rt_rob_op_trans_y character varying(50),
    br_rrf_rt_rob_op_trans_z character varying(50),
    br_rrf_rt_ptv_marg_x character varying(50),
    br_rrf_rt_ptv_marg_y character varying(50),
    br_rrf_rt_ptv_marg_z character varying(50),
    br_rrf_rt_rob_eval character varying(50),
    br_rrf_rt_rob_eval_trans_x character varying(50),
    br_rrf_rt_rob_eval_trans_y character varying(50),
    br_rrf_rt_rob_eval_trans_z character varying(50),
    br_rrf_rt_rob_eval_range_unc_use character varying(50),
    br_rrf_rt_rob_eval_range_unc character varying(50),
    br_rrf_rt_rob_eval_rot_use character varying(50),
    br_rrf_rt_rob_eval_rot_pitch character varying(50),
    br_rrf_rt_rob_eval_rot_roll character varying(50),
    br_rrf_rt_rob_eval_rot_yaw character varying(50),
    br_rrf_rt_imaging character varying(50),
    br_rrf_rt_imaging_other character varying(50),
    br_rrf_rt_pos_cor character varying(50),
    br_rrf_rt_nr_isoc character varying(50),
    br_rrf_rt_dose_eng character varying(50),
    br_rrf_rt_mc_unc character varying(50),
    br_rrf_rt_treatment character varying(50),
    br_rrf_rt_rt_techn_pho character varying(50),
    br_rrf_rt_rt_techn_pro character varying(50),
    br_rrf_rt_repaint character varying(50),
    br_rrf_rt_repaint_nr_volume character varying(50),
    br_rrf_rt_repaint_nr_layer character varying(50),
    br_rrf_rt_beam_absorb character varying(50),
    br_rrf_seq_rt character varying(50),
    br_rrf_treatm_pos character varying(50),
    br_rrf_treatm_pos_other character varying(50),
    br_rrf_arm_pos character varying(50),
    br_rrf_arm_pos_other character varying(50),
    br_rrf_plan_mri character varying(50),
    br_rrf_breast character varying(50),
    br_rrf_part_breast character varying(50),
    br_rrf_chest_wall character varying(50),
    br_rrf_level1_2 character varying(50),
    br_rrf_level3_4 character varying(50),
    br_rrf_interpec_nodes character varying(50),
    br_rrf_intern_mchain character varying(50),
    br_rrf_mot_manag_tech character varying(50),
    br_rrf_bolus character varying(50),
    br_rrf_adapt_str character varying(50),
    br_rrf_boost_tech character varying(50),
    br_rrf_dose_prescr character varying(50),
    br_rrf_fr_dose_elec_r character varying(50),
    br_rrf_nr_fr_elec_reg character varying(50),
    br_rrf_fr_dose_boost character varying(50),
    br_rrf_nr_fr_boost_reg character varying(50),
    br_rrf_boost_vol character varying(50),
    br_rrf_cmam_vol character varying(50),
    br_rrf_dmean_ptv_elec character varying(50),
    br_rrf_v95_ptv_elec character varying(50),
    br_rrf_v94_ptv_elec character varying(50),
    br_rrf_v93_ptv_elec character varying(50),
    br_rrf_d98_ptv_elec character varying(50),
    br_rrf_d50_elec character varying(50),
    br_rrf_d2_ptv_elec character varying(50),
    br_rrf_dmean_ptv_boost character varying(50),
    br_rrf_v95_ptv_boost character varying(50),
    br_rrf_v94_ptv_boost character varying(50),
    br_rrf_v93_ptv_boost character varying(50),
    br_rrf_d98_ptv_boost character varying(50),
    br_rrf_d50_boost character varying(50),
    br_rrf_d2_ptv_boost character varying(50),
    br_rrf_v95_pat_boost character varying(50),
    br_rrf_oar_cbreast_use character varying(50),
    br_rrf_oar_cbreast_md character varying(50),
    br_rrf_oar_cbreast_v1 character varying(50),
    br_rrf_oar_lungtot_use character varying(50),
    br_rrf_oar_lungtot_md character varying(50),
    br_rrf_oar_lungtot_v20 character varying(50),
    br_rrf_oar_heart_use character varying(50),
    br_rrf_oar_heart_md character varying(50),
    br_rrf_oar_thyroid_use character varying(50),
    br_rrf_oar_thyroid_md character varying(50),
    br_rrf_oar_thyroid_d2 character varying(50),
    br_rrf_oar_thyroid_d2m character varying(50),
    br_rrf_oar_oesoph_use character varying(50),
    br_rrf_oar_oesoph_md character varying(50),
    br_rrf_oar_oesoph_d2 character varying(50),
    br_rrf_oar_oesoph_d2m character varying(50),
    br_rrf_oar_lungl_use character varying(50),
    br_rrf_oar_lungl_md character varying(50),
    br_rrf_oar_lungl_v20 character varying(50),
    br_rrf_oar_lungr_use character varying(50),
    br_rrf_oar_lungr_md character varying(50),
    br_rrf_oar_lungr_v20 character varying(50),
    br_rrf_oar_body_use character varying(50),
    br_rrf_oar_body_md character varying(50),
    br_rrf_oar_body_d2 character varying(50),
    br_rrf_oar_body_d2m character varying(50),
    br_rrf_oar_atriuml_use character varying(50),
    br_rrf_oar_atriuml_md character varying(50),
    br_rrf_oar_atriuml_v10 character varying(50),
    br_rrf_oar_atriuml_v5 character varying(50),
    br_rrf_oar_atriuml_d2 character varying(50),
    br_rrf_oar_atriuml_d2m character varying(50),
    br_rrf_oar_atriumr_use character varying(50),
    br_rrf_oar_atriumr_md character varying(50),
    br_rrf_oar_atriumr_v10 character varying(50),
    br_rrf_oar_atriumr_v5 character varying(50),
    br_rrf_oar_atriumr_d2 character varying(50),
    br_rrf_oar_atriumr_d2m character varying(50),
    br_rrf_oar_ventrl_use character varying(50),
    br_rrf_oar_ventrl_md character varying(50),
    br_rrf_oar_ventrl_v10 character varying(50),
    br_rrf_oar_ventrl_v5 character varying(50),
    br_rrf_oar_ventrl_d2 character varying(50),
    br_rrf_oar_ventrl_d2m character varying(50),
    br_rrf_oar_ventrr_use character varying(50),
    br_rrf_oar_ventrr_md character varying(50),
    br_rrf_oar_ventrr_v10 character varying(50),
    br_rrf_oar_ventrr_v5 character varying(50),
    br_rrf_oar_ventrr_d2 character varying(50),
    br_rrf_oar_ventrr_d2m character varying(50),
    br_rrf_oar_rca_use character varying(50),
    br_rrf_oar_rca_md character varying(50),
    br_rrf_oar_rca_v10 character varying(50),
    br_rrf_oar_rca_v5 character varying(50),
    br_rrf_oar_rca_d2 character varying(50),
    br_rrf_oar_rca_d2m character varying(50),
    br_rrf_oar_lca_use character varying(50),
    br_rrf_oar_lca_md character varying(50),
    br_rrf_oar_lca_v10 character varying(50),
    br_rrf_oar_lca_v5 character varying(50),
    br_rrf_oar_lca_d2 character varying(50),
    br_rrf_oar_lca_d2m character varying(50),
    br_rrf_oar_cx_use character varying(50),
    br_rrf_oar_cx_md character varying(50),
    br_rrf_oar_cx_v10 character varying(50),
    br_rrf_oar_cx_v5 character varying(50),
    br_rrf_oar_cx_d2 character varying(50),
    br_rrf_oar_cx_d2m character varying(50),
    br_rrf_oar_lad_use character varying(50),
    br_rrf_oar_lad_md character varying(50),
    br_rrf_oar_lad_v10 character varying(50),
    br_rrf_oar_lad_v5 character varying(50),
    br_rrf_oar_lad_d2 character varying(50),
    br_rrf_oar_lad_d2m character varying(50),
    br_rrf_oar_mv_use character varying(50),
    br_rrf_oar_mv_md character varying(50),
    br_rrf_oar_mv_v10 character varying(50),
    br_rrf_oar_mv_v5 character varying(50),
    br_rrf_oar_mv_d2 character varying(50),
    br_rrf_oar_mv_d2m character varying(50),
    br_rrf_oar_tv_use character varying(50),
    br_rrf_oar_tv_md character varying(50),
    br_rrf_oar_tv_v10 character varying(50),
    br_rrf_oar_tv_v5 character varying(50),
    br_rrf_oar_tv_d2 character varying(50),
    br_rrf_oar_tv_d2m character varying(50),
    br_rrf_oar_av_use character varying(50),
    br_rrf_oar_av_md character varying(50),
    br_rrf_oar_av_v10 character varying(50),
    br_rrf_oar_av_v5 character varying(50),
    br_rrf_oar_av_d2 character varying(50),
    br_rrf_oar_av_d2m character varying(50),
    br_rrf_oar_pv_use character varying(50),
    br_rrf_oar_pv_md character varying(50),
    br_rrf_oar_pv_v10 character varying(50),
    br_rrf_oar_pv_v5 character varying(50),
    br_rrf_oar_pv_d2 character varying(50),
    br_rrf_oar_pv_d2m character varying(50),
    br_rrf_ph_dmean_ptv_elec character varying(50),
    br_rrf_ph_v95_ptv_elec character varying(50),
    br_rrf_ph_d98_ptv_elec character varying(50),
    br_rrf_ph_d50_elec character varying(50),
    br_rrf_ph_d2_ptv_elec character varying(50),
    br_rrf_ph_dmean_ptv_boost character varying(50),
    br_rrf_ph_v95_ptv_boost character varying(50),
    br_rrf_ph_d98_ptv_boost character varying(50),
    br_rrf_ph_d50_boost character varying(50),
    br_rrf_ph_d2_ptv_boost character varying(50),
    br_rrf_ph_v95_pat_boost character varying(50),
    br_rrf_oar_ph_cbreast_use character varying(50),
    br_rrf_oar_ph_cbreast_md character varying(50),
    br_rrf_oar_ph_cbreast_v1 character varying(50),
    br_rrf_oar_ph_lungtot_use character varying(50),
    br_rrf_oar_ph_lungtot_md character varying(50),
    br_rrf_oar_ph_lungtot_v20 character varying(50),
    br_rrf_oar_ph_heart_use character varying(50),
    br_rrf_oar_ph_heart_md character varying(50),
    br_rrf_oar_ph_thyroid_use character varying(50),
    br_rrf_oar_ph_thyroid_md character varying(50),
    br_rrf_oar_ph_thyroid_d2 character varying(50),
    br_rrf_oar_ph_oesoph_use character varying(50),
    br_rrf_oar_ph_oesoph_md character varying(50),
    br_rrf_oar_ph_oesoph_d2 character varying(50),
    br_rrf_oar_ph_lungl_use character varying(50),
    br_rrf_oar_ph_lungl_md character varying(50),
    br_rrf_oar_ph_lungl_v20 character varying(50),
    br_rrf_oar_ph_lungr_use character varying(50),
    br_rrf_oar_ph_lungr_md character varying(50),
    br_rrf_oar_ph_lungr_v20 character varying(50),
    br_rrf_oar_ph_body_use character varying(50),
    br_rrf_oar_ph_body_md character varying(50),
    br_rrf_oar_ph_body_d2 character varying(50),
    br_rrf_oar_ph_atriuml_use character varying(50),
    br_rrf_oar_ph_atriuml_md character varying(50),
    br_rrf_oar_ph_atriuml_v10 character varying(50),
    br_rrf_oar_ph_atriuml_v5 character varying(50),
    br_rrf_oar_ph_atriuml_d2 character varying(50),
    br_rrf_oar_ph_atriumr_use character varying(50),
    br_rrf_oar_ph_atriumr_md character varying(50),
    br_rrf_oar_ph_atriumr_v10 character varying(50),
    br_rrf_oar_ph_atriumr_v5 character varying(50),
    br_rrf_oar_ph_atriumr_d2 character varying(50),
    br_rrf_oar_ph_ventrl_use character varying(50),
    br_rrf_oar_ph_ventrl_md character varying(50),
    br_rrf_oar_ph_ventrl_v10 character varying(50),
    br_rrf_oar_ph_ventrl_v5 character varying(50),
    br_rrf_oar_ph_ventrl_d2 character varying(50),
    br_rrf_oar_ph_ventrr_use character varying(50),
    br_rrf_oar_ph_ventrr_md character varying(50),
    br_rrf_oar_ph_ventrr_v10 character varying(50),
    br_rrf_oar_ph_ventrr_v5 character varying(50),
    br_rrf_oar_ph_ventrr_d2 character varying(50),
    br_rrf_oar_ph_rca_use character varying(50),
    br_rrf_oar_ph_rca_md character varying(50),
    br_rrf_oar_ph_rca_v10 character varying(50),
    br_rrf_oar_ph_rca_v5 character varying(50),
    br_rrf_oar_ph_rca_d2 character varying(50),
    br_rrf_oar_ph_lca_use character varying(50),
    br_rrf_oar_ph_lca_md character varying(50),
    br_rrf_oar_ph_lca_v10 character varying(50),
    br_rrf_oar_ph_lca_v5 character varying(50),
    br_rrf_oar_ph_lca_d2 character varying(50),
    br_rrf_oar_ph_cx_use character varying(50),
    br_rrf_oar_ph_cx_md character varying(50),
    br_rrf_oar_ph_cx_v10 character varying(50),
    br_rrf_oar_ph_cx_v5 character varying(50),
    br_rrf_oar_ph_cx_d2 character varying(50),
    br_rrf_oar_ph_lad_use character varying(50),
    br_rrf_oar_ph_lad_md character varying(50),
    br_rrf_oar_ph_lad_v10 character varying(50),
    br_rrf_oar_ph_lad_v5 character varying(50),
    br_rrf_oar_ph_lad_d2 character varying(50),
    br_rrf_oar_ph_mv_use character varying(50),
    br_rrf_oar_ph_mv_md character varying(50),
    br_rrf_oar_ph_mv_v10 character varying(50),
    br_rrf_oar_ph_mv_v5 character varying(50),
    br_rrf_oar_ph_mv_d2 character varying(50),
    br_rrf_oar_ph_tv_use character varying(50),
    br_rrf_oar_ph_tv_md character varying(50),
    br_rrf_oar_ph_tv_v10 character varying(50),
    br_rrf_oar_ph_tv_v5 character varying(50),
    br_rrf_oar_ph_tv_d2 character varying(50),
    br_rrf_oar_ph_av_use character varying(50),
    br_rrf_oar_ph_av_md character varying(50),
    br_rrf_oar_ph_av_v10 character varying(50),
    br_rrf_oar_ph_av_v5 character varying(50),
    br_rrf_oar_ph_av_d2 character varying(50),
    br_rrf_oar_ph_pv_use character varying(50),
    br_rrf_oar_ph_pv_md character varying(50),
    br_rrf_oar_ph_pv_v10 character varying(50),
    br_rrf_oar_ph_pv_v5 character varying(50),
    br_rrf_oar_ph_pv_d2 character varying(50),
    br_rrf_thc character varying(50),
    br_rrf_date_start_rt character varying(50),
    br_rrf_date_last_rt character varying(50),
    br_rrf_trt_planname1 character varying(50),
    br_rrf_trt_totdose1 character varying(50),
    br_rrf_trt_fract1 character varying(50),
    br_rrf_trt_tecbr1 character varying(50),
    br_rrf_trt_planname2 character varying(50),
    br_rrf_trt_totdose2 character varying(50),
    br_rrf_trt_fract2 character varying(50),
    br_rrf_trt_tecbr2 character varying(50),
    br_rrf_trt_planname3 character varying(50),
    br_rrf_trt_totdose3 character varying(50),
    br_rrf_trt_fract3 character varying(50),
    br_rrf_trt_tecbr3 character varying(50),
    br_rrf_trt_planname4 character varying(50),
    br_rrf_trt_totdose4 character varying(50),
    br_rrf_trt_fract4 character varying(50),
    br_rrf_trt_tecbr4 character varying(50),
    br_rrf_trt_planname5 character varying(50),
    br_rrf_trt_totdose5 character varying(50),
    br_rrf_trt_fract5 character varying(50),
    br_rrf_trt_tecbr5 character varying(50),
    br_rise_date_consult date,
    br_rise_dermatitis character varying(250),
    br_rise_armoedema character varying(250),
    br_rise_pain_chestw_breast character varying(50),
    br_rise_dysphagia character varying(50),
    br_rise_telangie character varying(50),
    br_rise_brach_plex1 character varying(50),
    br_rise_brach_plex2 character varying(50),
    br_rise_brach_plex_ctcae character varying(50),
    br_rise_ribfract1 character varying(50),
    br_rise_ribfract2 character varying(50),
    br_rise_ribfract3 character varying(50),
    br_rise_ribfract_ctcae character varying(50),
    br_rise_rad_pneum character varying(50),
    br_rise_rad_pneum_ctcae character varying(50),
    br_rise_chron_painmed character varying(50),
    br_rise_hypertension character varying(50),
    br_rise_hyperchol character varying(50),
    br_rise_dyslip character varying(50),
    br_rise_dvtrom_lungemb character varying(50),
    br_rise_ap character varying(50),
    br_rise_ap_date date,
    br_rise_cardiac_death character varying(50),
    br_rise_cardiac_death_date date,
    br_rise_arrhythmia character varying(50),
    br_rise_arrhythmia_date date,
    br_rise_cardiomyop character varying(50),
    br_rise_cardiomyop_date date,
    br_rise_cardiac_valve character varying(50),
    br_rise_cardiac_valve_date date,
    br_rise_coron_revasc character varying(50),
    br_rise_coron_revasc_date date,
    br_rise_hypothyr character varying(50),
    br_rise_hypothyr_date date,
    br_rise_mi character varying(50),
    br_rise_mi_date date,
    br_rise_heart_fail character varying(50),
    br_rise_heart_fail_date date,
    br_rise_claudication character varying(50),
    br_rise_aortic_aneurysm character varying(50),
    br_rise_cva character varying(50),
    br_rise_tia character varying(50),
    br_rise_dm character varying(50),
    br_rise_dm_status character varying(50),
    br_rise_demen character varying(50),
    br_rise_copd character varying(50),
    br_rise_con_tis_d character varying(50),
    br_rise_pep_ul_d character varying(50),
    br_rise_liv_d character varying(50),
    br_rise_hemip character varying(50),
    br_rise_ckd character varying(50),
    br_rise_prev_sol_tum character varying(50),
    br_rise_prev_leuk character varying(50),
    br_rise_prev_lymph character varying(50)
);


ALTER TABLE public.br_data OWNER TO postgres;

--
-- Name: eortc_bn20; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eortc_bn20 (
    eortc_bn20_id character varying(50) NOT NULL,
    gen_idnumber character varying(50),
    eortc_bn20_timepoint character varying(50),
    eortc_bn20_date date,
    eortc_bn20_feel_insecure_future character varying(50),
    eortc_bn20_feel_relapse character varying(50),
    eortc_bn20_concern_family character varying(50),
    eortc_bn20_headache character varying(50),
    eortc_bn20_view_future character varying(50),
    eortc_bn20_see_double character varying(50),
    eortc_bn20_out_of_focus character varying(50),
    eortc_bn20_trouble_read character varying(50),
    eortc_bn20_seizures character varying(50),
    eortc_bn20_muscle_weak_bodyside character varying(50),
    eortc_bn20_trouble_words character varying(50),
    eortc_bn20_trouble_speaking character varying(50),
    eortc_bn20_trouble_thoughts character varying(50),
    eortc_bn20_drowsy character varying(50),
    eortc_bn20_coordination character varying(50),
    eortc_bn20_hairloss character varying(50),
    eortc_bn20_itchy_skin character varying(50),
    eortc_bn20_muscle_weak_legs character varying(50),
    eortc_bn20_insecure_feet character varying(50),
    eortc_bn20_trouble_pee character varying(50)
);


ALTER TABLE public.eortc_bn20 OWNER TO postgres;

--
-- Name: eortc_br23; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eortc_br23 (
    br23_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    br23_timepoint character varying(50),
    br23_qr character varying(50),
    br23_date date,
    br23_dry_mouth character varying(150),
    br23_taste character varying(150),
    br23_eyes character varying(150),
    br23_hair_loss character varying(150),
    br23_hair_loss_upset character varying(150),
    br23_unwell character varying(150),
    br23_hot_flashes character varying(150),
    br23_headache character varying(150),
    br23_feel_less_attract character varying(150),
    br23_feel_less_feminine character varying(150),
    br23_diff_see_naked character varying(150),
    br23_dissatisfied_body character varying(150),
    br23_worried_future character varying(150),
    br23_feel_sex character varying(150),
    br23_sex_active character varying(150),
    br23_sex_active_enjoy character varying(150),
    br23_pain_arm character varying(150),
    br23_swollen_arm character varying(150),
    br23_move_arm character varying(150),
    br23_pain_chest character varying(150),
    br23_breast_swollen character varying(150),
    br23_breast_hypersensitive character varying(150),
    br23_skin_problems character varying(150)
);


ALTER TABLE public.eortc_br23 OWNER TO postgres;

--
-- Name: eortc_c30; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eortc_c30 (
    eortc_c30_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    eortc_c30_timepoint character varying(50),
    eortc_c30_qr character varying(50),
    eortc_c30_date date,
    eortc_c30_stren_act character varying(50),
    eortc_c30_long_walk character varying(50),
    eortc_c30_short_walk character varying(50),
    eortc_c30_bedchair_day character varying(50),
    eortc_c30_help_adl character varying(50),
    eortc_c30_limit_act character varying(50),
    eortc_c30_limit_hobbies character varying(50),
    eortc_c30_dyspnoea character varying(50),
    eortc_c30_pain character varying(50),
    eortc_c30_rest character varying(50),
    eortc_c30_sleep character varying(50),
    eortc_c30_weak character varying(50),
    eortc_c30_appetite character varying(50),
    eortc_c30_nausea character varying(50),
    eortc_c30_vomit character varying(50),
    eortc_c30_constip character varying(50),
    eortc_c30_diarrhea character varying(50),
    eortc_c30_fatigue character varying(50),
    eortc_c30_interf_pain character varying(50),
    eortc_c30_concentr character varying(50),
    eortc_c30_tense character varying(50),
    eortc_c30_worry character varying(50),
    eortc_c30_irritable character varying(50),
    eortc_c30_depressed character varying(50),
    eortc_c30_memory character varying(50),
    eortc_c30_fam_life character varying(50),
    eortc_c30_soc_act character varying(50),
    eortc_c30_financial character varying(50),
    eortc_c30_health character varying(50),
    eortc_c30_qol character varying(50)
);


ALTER TABLE public.eortc_c30 OWNER TO postgres;

--
-- Name: eortc_hn35; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eortc_hn35 (
    eortc_hn35_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    eortc_hn35_timepoint character varying(50),
    eortc_hn35_qr character varying(50),
    eortc_hn35_date date,
    eortc_hn35_pain_mouth character varying(50),
    eortc_hn35_pain_jaw character varying(50),
    eortc_hn35_sore_mouth character varying(50),
    eortc_hn35_pain_throat character varying(50),
    eortc_hn35_swal_liq character varying(50),
    eortc_hn35_swal_pur_food character varying(50),
    eortc_hn35_swal_sol_food character varying(50),
    eortc_hn35_choke character varying(50),
    eortc_hn35_teeth character varying(50),
    eortc_hn35_open_mouth character varying(50),
    eortc_hn35_dry_mouth character varying(50),
    eortc_hn35_sticky_saliva character varying(50),
    eortc_hn35_sense_smell character varying(50),
    eortc_hn35_sense_taste character varying(50),
    eortc_hn35_cough character varying(50),
    eortc_hn35_hoarse character varying(50),
    eortc_hn35_ill character varying(50),
    eortc_hn35_appearance character varying(50),
    eortc_hn35_eating character varying(50),
    eortc_hn35_eating_family character varying(50),
    eortc_hn35_eating_people character varying(50),
    eortc_hn35_meal_enjoy character varying(50),
    eortc_hn35_talk_people character varying(50),
    eortc_hn35_talk_telephone character varying(50),
    eortc_hn35_contact_fam character varying(50),
    eortc_hn35_contact_friends character varying(50),
    eortc_hn35_out_public character varying(50),
    eortc_hn35_phys_contact character varying(50),
    eortc_hn35_pain_killers character varying(50),
    eortc_hn35_nutr_suppl character varying(50),
    eortc_hn35_feed_tube character varying(50),
    eortc_hn35_lost_weight character varying(50),
    eortc_hn35_gain_weight character varying(50)
);


ALTER TABLE public.eortc_hn35 OWNER TO postgres;

--
-- Name: eq_5d; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eq_5d (
    eq_5d_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    eq_5d_timepoint character varying(50),
    eq_5d_qr character varying(50),
    eq_5d_date date,
    eq_5d_mobility character varying(50),
    eq_5d_selfcare character varying(50),
    eq_5d_usual_act character varying(50),
    eq_5d_pain_discomf character varying(50),
    eq_5d_anx_depres character varying(50),
    eq_5d_scale_score character varying(50)
);


ALTER TABLE public.eq_5d OWNER TO postgres;

--
-- Name: gen_alcohol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gen_alcohol (
    gen_alcohol_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    gen_alcohol character varying(50),
    gen_alcohol_days character varying(50),
    gen_alcohol_glass character varying(50)
);


ALTER TABLE public.gen_alcohol OWNER TO postgres;

--
-- Name: gen_other_cancer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gen_other_cancer (
    gen_other_cancer_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    gen_oth_c_icd character varying(50),
    gen_oth_c_site character varying(50),
    gen_oth_c_date date,
    gen_oth_c_rt character varying(50),
    gen_othercancer character varying(50),
    gen_reirradiation character varying(50)
);


ALTER TABLE public.gen_other_cancer OWNER TO postgres;

--
-- Name: gen_patient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gen_patient (
    gen_idnumber character varying(50) NOT NULL,
    gen_treat_centre character varying(100),
    gen_refer_centre character varying(100),
    gen_date_registr date,
    gen_year_birth integer,
    gen_age integer,
    gen_gender character varying(10),
    gen_education character varying(50),
    gen_relation character varying(20),
    gen_weight real,
    gen_height real,
    gen_date_diag date,
    gen_tumoursite character varying(200),
    gen_rt_treatment character varying(50),
    gen_oth_c_rt_reirr character varying(50)
);


ALTER TABLE public.gen_patient OWNER TO postgres;

--
-- Name: gen_plan_comparison; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gen_plan_comparison (
    gen_plan_comparison_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    gen_plan_comparison character varying(50),
    gen_plan_comp_date date,
    gen_plan_comp_version character varying(50),
    gen_comp_outcome character varying(600),
    gen_dec_protons character varying(50),
    gen_reason_protons character varying(50),
    gen_reason_prot_other character varying(50)
);


ALTER TABLE public.gen_plan_comparison OWNER TO postgres;

--
-- Name: gen_smoking; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gen_smoking (
    gen_smoking_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    gen_smoking character varying(50),
    gen_sm_packyears integer,
    gen_sm_stopmonths integer
);


ALTER TABLE public.gen_smoking OWNER TO postgres;

--
-- Name: hn_bl; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hn_bl (
    hn_bl_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    hn_bl_weight_loss integer,
    hn_bl_reirr character varying(50),
    hn_bl_treatm_loc_recur character varying(50),
    hn_bl_treatm_reg_recur character varying(50),
    hn_bl_ct character varying(50),
    hn_bl_petct character varying(50),
    hn_bl_mri character varying(50),
    hn_bl_ultras character varying(50),
    hn_bl_sn character varying(50),
    hn_bl_tumour_site character varying(50),
    hn_bl_tumour_site_oth character varying(50),
    hn_bl_histo character varying(50),
    hn_bl_histo_date date,
    hn_bl_tstage_7 character varying(50),
    hn_bl_tstage_7_add character varying(50),
    hn_bl_nstage_7 character varying(50),
    hn_bl_mstage_7 character varying(50),
    hn_bl_tstage_8 character varying(50),
    hn_bl_tstage_8_add character varying(50),
    hn_bl_nstage_8 character varying(50),
    hn_bl_mstage_8 character varying(50),
    hn_bl_p16 character varying(50),
    hn_bl_hpv character varying(50),
    hn_bl_ebv character varying(50),
    hn_bl_systtr character varying(50),
    hn_bl_surg_tumour character varying(50),
    hn_bl_surg_tum_date date,
    hn_bl_surg_ptstage character varying(50),
    hn_bl_surg_surg_marg character varying(50),
    hn_bl_surg_max_diam integer,
    hn_bl_surg_depth_infil integer,
    hn_bl_surg_angio character varying(50),
    hn_bl_surg_pering character varying(50),
    hn_bl_surg_infltr_gr character varying(50),
    hn_bl_surg_neck character varying(50),
    hn_bl_surg_neck_date date,
    hn_bl_surg_neck_nstage character varying(50),
    hn_bl_surg_neck_ln_path integer,
    hn_bl_surg_neck_lnmeta integer,
    hn_bl_surg_neck_ln_ecs integer,
    hn_bl_prep_plan_dual_ct character varying(50),
    hn_bl_prep_plan_petct character varying(50),
    hn_bl_prep_plan_mri character varying(50),
    hn_bl_rt_rob_plan character varying(50),
    hn_bl_rt_rob_op_trans_x real,
    hn_bl_rt_rob_op_trans_y real,
    hn_bl_rt_rob_op_trans_z real,
    hn_bl_rt_ptv_marg_x real,
    hn_bl_rt_ptv_marg_y real,
    hn_bl_rt_ptv_marg_z real,
    hn_bl_rt_rob_eval character varying(50),
    hn_bl_rt_rob_eval_trans_x real,
    hn_bl_rt_rob_eval_trans_y real,
    hn_bl_rt_rob_eval_trans_z real,
    hn_bl_rt_rob_eval_range_unc_use character varying(50),
    hn_bl_rt_rob_eval_range_unc real,
    hn_bl_rt_rob_eval_rot_use character varying(50),
    hn_bl_rt_rob_eval_rot_pitch real,
    hn_bl_rt_rob_eval_rot_roll real,
    hn_bl_rt_rob_eval_rot_yaw real,
    hn_bl_rt_imaging character varying(50),
    hn_bl_rt_imaging_other character varying(50),
    hn_bl_rt_pos_cor character varying(50),
    hn_bl_rt_nr_isoc integer,
    hn_bl_rt_dose_eng character varying(50),
    hn_bl_rt_mc_unc real,
    hn_bl_rt_treatment character varying(50),
    hn_bl_rt_rt_techn_bl_pho character varying(50),
    hn_bl_rt_rt_techn_bl_pro character varying(50),
    hn_bl_rt_repaint character varying(50),
    hn_bl_rt_repaint_nr_volume character varying(50),
    hn_bl_rt_repaint_nr_layer character varying(50),
    hn_bl_rt_beam_absorb character varying(50),
    hn_bl_rt_plan_adapt_strat character varying(50),
    hn_bl_rt_plan_boost character varying(50),
    hn_bl_prep_plan_tarvol character varying(50),
    hn_bl_prep_plan_gtv real,
    hn_bl_prep_plan_ctv1 real,
    hn_bl_prep_plan_ctv2 real,
    hn_bl_prep_plan_ctv3 real,
    hn_bl_therrt_oar_paro_r_use character varying(50),
    hn_bl_therrt_oar_paro_r_md real,
    hn_bl_therrt_oar_paro_l_use character varying(50),
    hn_bl_therrt_oar_paro_l_md real,
    hn_bl_therrt_oar_subm_r_use character varying(50),
    hn_bl_therrt_oar_subm_r_md real,
    hn_bl_therrt_oar_subm_l_use character varying(50),
    hn_bl_therrt_oar_subm_l_md real,
    hn_bl_therrt_oar_ext_oc_use character varying(50),
    hn_bl_therrt_oar_ext_oc_md real,
    hn_bl_therrt_oar_pcm_sup_use character varying(50),
    hn_bl_therrt_oar_pcm_sup_md real,
    hn_bl_therrt_oar_pcm_med_use character varying(50),
    hn_bl_therrt_oar_pcm_med_md real,
    hn_bl_therrt_oar_pcm_inf_use character varying(50),
    hn_bl_therrt_oar_pcm_inf_md real,
    hn_bl_therrt_oar_ant_ey_r_use character varying(50),
    hn_bl_therrt_oar_ant_ey_r_md real,
    hn_bl_therrt_oar_ant_ey_l_use character varying(50),
    hn_bl_therrt_oar_ant_ey_l_md real,
    hn_bl_therrt_oar_post_ey_r_use character varying(50),
    hn_bl_therrt_oar_post_ey_r_md real,
    hn_bl_therrt_oar_post_ey_l_use character varying(50),
    hn_bl_therrt_oar_post_ey_l_md real,
    hn_bl_therrt_oar_lacr_r_use character varying(50),
    hn_bl_therrt_oar_lacr_r_md real,
    hn_bl_therrt_oar_lacr_l_use character varying(50),
    hn_bl_therrt_oar_lacr_l_md real,
    hn_bl_therrt_oar_bumu_r_use character varying(50),
    hn_bl_therrt_oar_bumu_r_md real,
    hn_bl_therrt_oar_bumu_l_use character varying(50),
    hn_bl_therrt_oar_bumu_l_md real,
    hn_bl_therrt_oar_mand_use character varying(50),
    hn_bl_therrt_oar_mand_md real,
    hn_bl_therrt_oar_mand_maxd character varying(50),
    hn_bl_therrt_oar_mand_maxdm real,
    hn_bl_therrt_oar_coch_r_use character varying(50),
    hn_bl_therrt_oar_coch_r_md real,
    hn_bl_therrt_oar_coch_l_use character varying(50),
    hn_bl_therrt_oar_coch_l_md real,
    hn_bl_therrt_oar_supglot_la_use character varying(50),
    hn_bl_therrt_oar_supglot_la_md real,
    hn_bl_therrt_oar_glot_use character varying(50),
    hn_bl_therrt_oar_glot_md real,
    hn_bl_therrt_oar_art_use character varying(50),
    hn_bl_therrt_oar_art_md real,
    hn_bl_therrt_oar_cric_use character varying(50),
    hn_bl_therrt_oar_cric_md real,
    hn_bl_therrt_oar_c_oes_use character varying(50),
    hn_bl_therrt_oar_c_oes_md real,
    hn_bl_therrt_oar_thy_use character varying(50),
    hn_bl_therrt_oar_thy_md real,
    hn_bl_therrt_oar_brn_use character varying(50),
    hn_bl_therrt_oar_brn_md real,
    hn_bl_therrt_oar_brn_maxd real,
    hn_bl_therrt_oar_brn_maxdm real,
    hn_bl_therrt_oar_crbr_use character varying(50),
    hn_bl_therrt_oar_crbr_md real,
    hn_bl_therrt_oar_crbr_maxd real,
    hn_bl_therrt_oar_crbr_maxdm real,
    hn_bl_therrt_oar_crbl_use character varying(50),
    hn_bl_therrt_oar_crbl_md real,
    hn_bl_therrt_oar_crbl_maxd real,
    hn_bl_therrt_oar_crbl_maxdm real,
    hn_bl_therrt_oar_brnst_use character varying(50),
    hn_bl_therrt_oar_brnst_md real,
    hn_bl_therrt_oar_brnst_maxd real,
    hn_bl_therrt_oar_brnst_maxdm real,
    hn_bl_therrt_oar_pit_use character varying(50),
    hn_bl_therrt_oar_pit_md real,
    hn_bl_therrt_oar_opt_chi_use character varying(50),
    hn_bl_therrt_oar_opt_chi_maxd real,
    hn_bl_therrt_oar_opt_chi_maxdm real,
    hn_bl_therrt_oar_opt_nv_r_use character varying(50),
    hn_bl_therrt_oar_opt_nv_r_maxd real,
    hn_bl_therrt_oar_opt_nv_r_maxdm real,
    hn_bl_therrt_oar_opt_nv_l_use character varying(50),
    hn_bl_therrt_oar_opt_nv_l_maxd real,
    hn_bl_therrt_oar_opt_nv_l_maxdm real,
    hn_bl_therrt_oar_spine_use character varying(50),
    hn_bl_therrt_oar_spine_maxd real,
    hn_bl_therrt_oar_spine_maxdm real,
    hn_bl_therrt_oar_car_r_use character varying(50),
    hn_bl_therrt_oar_car_r_maxd real,
    hn_bl_therrt_oar_car_r_maxdm real,
    hn_bl_therrt_oar_car_l_use character varying(50),
    hn_bl_therrt_oar_car_l_maxd real,
    hn_bl_therrt_oar_car_l_maxdm real,
    hn_bl_therrt_ph_oar_paro_r_use character varying(50),
    hn_bl_therrt_ph_oar_paro_r_md real,
    hn_bl_therrt_ph_oar_paro_l_use character varying(50),
    hn_bl_therrt_ph_oar_paro_l_md real,
    hn_bl_therrt_ph_oar_subm_r_use character varying(50),
    hn_bl_therrt_ph_oar_subm_r_md real,
    hn_bl_therrt_ph_oar_subm_l_use character varying(50),
    hn_bl_therrt_ph_oar_subm_l_md real,
    hn_bl_therrt_ph_oar_ext_oc_use character varying(50),
    hn_bl_therrt_ph_oar_ext_oc_md real,
    hn_bl_therrt_ph_oar_pcm_sup_use character varying(50),
    hn_bl_therrt_ph_oar_pcm_sup_md real,
    hn_bl_therrt_ph_oar_pcm_med_use character varying(50),
    hn_bl_therrt_ph_oar_pcm_med_md real,
    hn_bl_therrt_ph_oar_pcm_inf_use character varying(50),
    hn_bl_therrt_ph_oar_pcm_inf_md real,
    hn_bl_therrt_ph_oar_ant_ey_r_use character varying(50),
    hn_bl_therrt_ph_oar_ant_ey_r_md real,
    hn_bl_therrt_ph_oar_ant_ey_l_use character varying(50),
    hn_bl_therrt_ph_oar_ant_ey_l_md real,
    hn_bl_therrt_ph_oar_post_ey_r_use character varying(50),
    hn_bl_therrt_ph_oar_post_ey_r_md real,
    hn_bl_therrt_ph_oar_post_ey_l_use character varying(50),
    hn_bl_therrt_ph_oar_post_ey_l_md real,
    hn_bl_therrt_ph_oar_lacr_r_use character varying(50),
    hn_bl_therrt_ph_oar_lacr_r_md real,
    hn_bl_therrt_ph_oar_lacr_l_use character varying(50),
    hn_bl_therrt_ph_oar_lacr_l_md real,
    hn_bl_therrt_ph_oar_bumu_r_use character varying(50),
    hn_bl_therrt_ph_oar_bumu_r_md real,
    hn_bl_therrt_ph_oar_bumu_l_use character varying(50),
    hn_bl_therrt_ph_oar_bumu_l_md real,
    hn_bl_therrt_ph_oar_mand_use character varying(50),
    hn_bl_therrt_ph_oar_mand_md real,
    hn_bl_therrt_ph_oar_mand_maxd real,
    hn_bl_therrt_ph_oar_coch_r_use character varying(50),
    hn_bl_therrt_ph_oar_coch_r_md real,
    hn_bl_therrt_ph_oar_coch_l_use character varying(50),
    hn_bl_therrt_ph_oar_coch_l_md real,
    hn_bl_therrt_ph_oar_supglot_la_use character varying(50),
    hn_bl_therrt_ph_oar_supglot_la_md real,
    hn_bl_therrt_ph_oar_glot_use character varying(50),
    hn_bl_therrt_ph_oar_glot_md real,
    hn_bl_therrt_ph_oar_art_use character varying(50),
    hn_bl_therrt_ph_oar_art_md real,
    hn_bl_therrt_ph_oar_cric_use character varying(50),
    hn_bl_therrt_ph_oar_cric_md real,
    hn_bl_therrt_ph_oar_c_oes_use character varying(50),
    hn_bl_therrt_ph_oar_c_oes_md real,
    hn_bl_therrt_ph_oar_thy_use character varying(50),
    hn_bl_therrt_ph_oar_thy_md real,
    hn_bl_therrt_ph_oar_brn_use character varying(50),
    hn_bl_therrt_ph_oar_brn_md real,
    hn_bl_therrt_ph_oar_brn_maxd real,
    hn_bl_therrt_ph_oar_crbr_use character varying(50),
    hn_bl_therrt_ph_oar_crbr_md real,
    hn_bl_therrt_ph_oar_crbr_maxd real,
    hn_bl_therrt_ph_oar_crbl_use character varying(50),
    hn_bl_therrt_ph_oar_crbl_md real,
    hn_bl_therrt_ph_oar_crbl_maxd real,
    hn_bl_therrt_ph_oar_brnst_use character varying(50),
    hn_bl_therrt_ph_oar_brnst_md real,
    hn_bl_therrt_ph_oar_brnst_maxd real,
    hn_bl_therrt_ph_oar_pit_use character varying(50),
    hn_bl_therrt_ph_oar_pit_md real,
    hn_bl_therrt_ph_oar_opt_chi_use character varying(50),
    hn_bl_therrt_ph_oar_opt_chi_maxd real,
    hn_bl_therrt_ph_oar_opt_nv_r_use character varying(50),
    hn_bl_therrt_ph_oar_opt_nv_r_maxd real,
    hn_bl_therrt_ph_oar_opt_nv_l_use character varying(50),
    hn_bl_therrt_ph_oar_opt_nv_l_maxd real,
    hn_bl_therrt_ph_oar_spine_use character varying(50),
    hn_bl_therrt_ph_oar_spine_maxd real,
    hn_bl_therrt_ph_oar_car_r_use character varying(50),
    hn_bl_therrt_ph_oar_car_r_maxd real,
    hn_bl_therrt_ph_oar_car_l_use character varying(50),
    hn_bl_therrt_ph_oar_car_l_maxd real,
    hn_bl_dose_high_dose real,
    hn_bl_dose_high_fr_dose real,
    hn_bl_dose_high_fr_n integer,
    hn_bl_dose_inter_fr_dose real,
    hn_bl_dose_inter_fr_n integer,
    hn_bl_dose_low_fr_dose real,
    hn_bl_dose_low_fr_n integer,
    hn_bl_tox_mi character varying(50),
    hn_bl_tox_heart_fail character varying(50),
    hn_bl_tox_per_vas_dis character varying(50),
    hn_bl_tox_cva_tia character varying(50),
    hn_bl_tox_demen character varying(50),
    hn_bl_tox_copd character varying(50),
    hn_bl_tox_con_tis_dis character varying(50),
    hn_bl_tox_pep_ulc_dis character varying(50),
    hn_bl_tox_liv_dis character varying(50),
    hn_bl_tox_dm character varying(50),
    hn_bl_tox_dm_status character varying(50),
    hn_bl_tox_hemip character varying(50),
    hn_bl_tox_ckd character varying(50),
    hn_bl_tox_prev_sol_tum character varying(50),
    hn_bl_tox_prev_leuk character varying(50),
    hn_bl_tox_prev_lymph character varying(50)
);


ALTER TABLE public.hn_bl OWNER TO postgres;

--
-- Name: hn_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hn_data (
    hn_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    hn_timepoint character varying(50),
    hn_data_entry_dt date,
    hn_bcf_weight_loss integer,
    hn_bcf_reirr character varying(50),
    hn_bcf_treatm_loc_recur character varying(50),
    hn_bcf_treatm_reg_recur character varying(50),
    hn_dpr_ct character varying(50),
    hn_dpr_petct character varying(50),
    hn_dpr_mri character varying(50),
    hn_dpr_ultras character varying(50),
    hn_dpr_sn character varying(50),
    hn_btf_tumour_site character varying(50),
    hn_btf_histo character varying(50),
    hn_btf_histo_date date,
    hn_btf_tstage_7 character varying(50),
    hn_btf_tstage_7_add character varying(50),
    hn_btf_nstage_7 character varying(50),
    hn_btf_mstage_7 character varying(50),
    hn_btf_tstage_8 character varying(50),
    hn_btf_tstage_8_add character varying(50),
    hn_btf_nstage_8 character varying(50),
    hn_btf_mstage_8 character varying(50),
    hn_btf_p16 character varying(50),
    hn_btf_hpv character varying(50),
    hn_btf_ebv character varying(50),
    hn_systtr_type character varying(50),
    hn_systtr_type_oth_concur character varying(250),
    hn_systtr_type_concur character varying(250),
    hn_systtr_cycl_concur integer,
    hn_systtr_start_concur date,
    hn_systtr_stop_concur date,
    hn_systtr_dose_red_concur character varying(50),
    hn_systtr_type_oth_concuradjuv_a character varying(250),
    hn_systtr_type_concuradjuv_a character varying(250),
    hn_systtr_cycl_concuradjuv_a integer,
    hn_systtr_start_concuradjuv_a date,
    hn_systtr_stop_concuradjuv_a date,
    hn_systtr_dose_red_concuradjuv_a character varying(50),
    hn_systtr_type_oth_induct character varying(250),
    hn_systtr_type_induct character varying(50),
    hn_systtr_cycl_induct integer,
    hn_systtr_start_induct date,
    hn_systtr_stop_induct date,
    hn_systtr_dose_red_induct character varying(50),
    hn_systtr_type_inductconcur character varying(50),
    hn_systtr_cycl_inductconcur integer,
    hn_systtr_start_inductconcur date,
    hn_systtr_stop_inductconcur date,
    hn_systtr_dose_red_inductconcur character varying(50),
    hn_pt_clin_trial character varying(50),
    hn_surg_tumour character varying(50),
    hn_surg_tum_date date,
    hn_surg_ptstage character varying(50),
    hn_surg_surg_marg character varying(50),
    hn_surg_max_diam integer,
    hn_surg_depth_infil integer,
    hn_surg_angio character varying(50),
    hn_surg_pering character varying(50),
    hn_surg_infltr_gr character varying(50),
    hn_surg_neck character varying(50),
    hn_surg_neck_date date,
    hn_surg_neck_nstage character varying(50),
    hn_surg_neck_ln_path integer,
    hn_surg_neck_lnmeta integer,
    hn_surg_neck_ln_ecs integer,
    hn_tox_weight real,
    hn_tox_dose_so_far real,
    hn_tox_xerostomia character varying(50),
    hn_tox_dysph character varying(50),
    hn_tox_dysph_umcg character varying(50),
    hn_tox_mucositis character varying(50),
    hn_tox_mucosa_rtog character varying(50),
    hn_tox_dermatitis character varying(50),
    hn_tox_osteoradion character varying(50),
    hn_tox_softtnecr character varying(50),
    hn_tox_mi character varying(50),
    hn_tox_heart_fail character varying(50),
    hn_tox_per_vas_dis character varying(50),
    hn_tox_cva_tia character varying(50),
    hn_tox_demen character varying(50),
    hn_tox_copd character varying(50),
    hn_tox_con_tis_dis character varying(50),
    hn_tox_pep_ulc_dis character varying(50),
    hn_tox_liv_dis character varying(50),
    hn_tox_dm character varying(50),
    hn_tox_dm_status character varying(50),
    hn_tox_hemip character varying(50),
    hn_tox_ckd character varying(50),
    hn_tox_prev_sol_tum character varying(50),
    hn_tox_prev_leuk character varying(50),
    hn_tox_prev_lymph character varying(50),
    hn_rrf_plan_dual_ct character varying(50),
    hn_rrf_plan_petct character varying(50),
    hn_rrf_plan_mri character varying(50),
    hn_rrf_rob_plan character varying(50),
    hn_rrf_rob_op_trans_x numeric(9,4),
    hn_rrf_rob_op_trans_y numeric(9,4),
    hn_rrf_rob_op_trans_z numeric(9,4),
    hn_rrf_ptv_marg_x numeric(9,4),
    hn_rrf_ptv_marg_y numeric(9,4),
    hn_rrf_ptv_marg_z numeric(9,4),
    hn_rrf_rob_eval character varying(50),
    hn_rrf_rob_eval_trans_x numeric(9,4),
    hn_rrf_rob_eval_trans_y numeric(9,4),
    hn_rrf_rob_eval_trans_z numeric(9,4),
    hn_rrf_rob_eval_range_unc character varying(50),
    hn_rrf_rob_eval_rot_pitch character varying(50),
    hn_rrf_rob_eval_rot_roll character varying(50),
    hn_rrf_rob_eval_rot_yaw character varying(50),
    hn_rrf_imaging character varying(50),
    hn_rrf_imaging_other character varying(50),
    hn_rrf_pos_cor character varying(50),
    hn_rrf_nr_isoc integer,
    hn_rrf_dose_eng character varying(50),
    hn_rrf_mc_unc numeric(9,4),
    hn_rrf_treatment character varying(50),
    hn_rrf_rt_techn_pho character varying(50),
    hn_rrf_rt_techn_pro character varying(50),
    hn_rrf_repaint character varying(50),
    hn_rrf_repaint_nr_volume integer,
    hn_rrf_repaint_nr_layer integer,
    hn_rrf_beam_absorb character varying(50),
    hn_rrf_plan_adapt_strat character varying(50),
    hn_rrf_plan_boost character varying(50),
    hn_rrf_tar_vol character varying(50),
    hn_rrf_pr_oar_paro_r_use character varying(50),
    hn_rrf_pr_oar_paro_r_md numeric(9,4),
    hn_rrf_pr_oar_paro_l_use character varying(50),
    hn_rrf_pr_oar_paro_l_md numeric(9,4),
    hn_rrf_pr_oar_subm_r_use character varying(50),
    hn_rrf_pr_oar_subm_r_md numeric(9,4),
    hn_rrf_pr_oar_subm_l_use character varying(50),
    hn_rrf_pr_oar_subm_l_md numeric(9,4),
    hn_rrf_pr_oar_ext_oc_use character varying(50),
    hn_rrf_pr_oar_ext_oc_md numeric(9,4),
    hn_rrf_pr_oar_pcm_sup_use character varying(50),
    hn_rrf_pr_oar_pcm_sup_md numeric(9,4),
    hn_rrf_pr_oar_pcm_med_use character varying(50),
    hn_rrf_pr_oar_pcm_med_md numeric(9,4),
    hn_rrf_pr_oar_pcm_inf_use character varying(50),
    hn_rrf_pr_oar_pcm_inf_md numeric(9,4),
    hn_rrf_ph_oar_paro_r_use character varying(50),
    hn_rrf_ph_oar_paro_r_md numeric(9,4),
    hn_rrf_ph_oar_paro_l_use character varying(50),
    hn_rrf_ph_oar_paro_l_md numeric(9,4),
    hn_rrf_ph_oar_subm_r_use character varying(50),
    hn_rrf_ph_oar_subm_r_md numeric(9,4),
    hn_rrf_ph_oar_subm_l_use character varying(50),
    hn_rrf_ph_oar_subm_l_md numeric(9,4),
    hn_rrf_ph_oar_ext_oc_use character varying(50),
    hn_rrf_ph_oar_ext_oc_md numeric(9,4),
    hn_rrf_ph_oar_pcm_sup_use character varying(50),
    hn_rrf_ph_oar_pcm_sup_md numeric(9,4),
    hn_rrf_ph_oar_pcm_med_use character varying(50),
    hn_rrf_ph_oar_pcm_med_md numeric(9,4),
    hn_rrf_ph_oar_pcm_inf_use character varying(50),
    hn_rrf_ph_oar_pcm_inf_md numeric(9,4),
    hn_rrf_dose_high_start date,
    hn_rrf_dose_high_stop date,
    hn_rrf_dose_high_dose numeric(9,4),
    hn_rrf_dose_high_fr_dose numeric(9,4),
    hn_rrf_dose_high_fr_n integer,
    hn_rrf_dose_inter_start date,
    hn_rrf_dose_inter_stop date,
    hn_rrf_dose_inter_fr_dose numeric(9,4),
    hn_rrf_dose_inter_fr_n integer,
    hn_rrf_dose_low_start date,
    hn_rrf_dose_low_stop date,
    hn_rrf_dose_low_fr_dose numeric(9,4),
    hn_rrf_dose_low_fr_n integer,
    hn_rrf_trt_planname1 character varying(50),
    hn_rrf_trt_totdose1 numeric(9,4),
    hn_rrf_trt_fract1 integer,
    hn_rrf_trt_techn1 character varying(50),
    hn_rrf_trt_planname2 character varying(50),
    hn_rrf_trt_totdose2 numeric(9,4),
    hn_rrf_trt_fract2 integer,
    hn_rrf_trt_techn2 character varying(50),
    hn_rrf_trt_planname3 character varying(50),
    hn_rrf_trt_totdose3 numeric(9,4),
    hn_rrf_trt_fract3 integer,
    hn_rrf_trt_techn3 character varying(50),
    hn_rrf_trt_planname4 character varying(50),
    hn_rrf_trt_totdose4 numeric(9,4),
    hn_rrf_trt_fract4 integer,
    hn_rrf_trt_techn4 character varying(50),
    hn_rrf_trt_planname5 character varying(50),
    hn_rrf_trt_totdose5 numeric(9,4),
    hn_rrf_trt_fract5 integer,
    hn_rrf_trt_techn5 character varying(50)
);


ALTER TABLE public.hn_data OWNER TO postgres;

--
-- Name: hn_ld; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hn_ld (
    hn_ld_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    hn_ld_thc character varying(50),
    hn_ld_pt_clin_trial character varying(50),
    hn_ld_systtr_type_induct character varying(50),
    hn_ld_systtr_type_oth_induct character varying(50),
    hn_ld_systtr_cycl_induct integer,
    hn_ld_systtr_start_induct date,
    hn_ld_systtr_stop_induct date,
    hn_ld_systtr_dose_red_induct character varying(50),
    hn_ld_systtr_type_concur character varying(250),
    hn_ld_systtr_type_oth_concur character varying(250),
    hn_ld_systtr_cycl_concur integer,
    hn_ld_systtr_start_concur date,
    hn_ld_systtr_stop_concur date,
    hn_ld_systtr_dose_red_concur character varying(50),
    hn_ld_systtr_type_concuradjuv_a character varying(250),
    hn_ld_systtr_type_oth_concuradjuv_a character varying(250),
    hn_ld_systtr_cycl_concuradjuv_a integer,
    hn_ld_systtr_start_concuradjuv_a date,
    hn_ld_systtr_stop_concuradjuv_a date,
    hn_ld_systtr_dose_red_concuradjuv_a character varying(50),
    hn_ld_dose_high_start date,
    hn_ld_dose_high_stop date,
    hn_ld_dose_inter_start date,
    hn_ld_dose_inter_stop date,
    hn_ld_dose_low_start date,
    hn_ld_dose_low_stop date,
    hn_ld_trt_planname1 character varying(50),
    hn_ld_trt_totdose1 real,
    hn_ld_trt_fract1 integer,
    hn_ld_trt_techn1 character varying(50),
    hn_ld_trt_planname2 character varying(50),
    hn_ld_trt_totdose2 real,
    hn_ld_trt_fract2 integer,
    hn_ld_trt_techn2 character varying(50),
    hn_ld_trt_planname3 character varying(50),
    hn_ld_trt_totdose3 real,
    hn_ld_trt_fract3 integer,
    hn_ld_trt_techn3 character varying(50),
    hn_ld_trt_planname4 character varying(50),
    hn_ld_trt_totdose4 real,
    hn_ld_trt_fract4 integer,
    hn_ld_trt_techn4 character varying(50),
    hn_ld_trt_planname5 character varying(50),
    hn_ld_trt_totdose5 real,
    hn_ld_trt_fract5 integer,
    hn_ld_trt_techn5 character varying(50)
);


ALTER TABLE public.hn_ld OWNER TO postgres;

--
-- Name: hn_tfu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hn_tfu (
    hn_tfu_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    hn_tfu_timepoint character varying(50),
    hn_tfu_date date,
    hn_tfu_status character varying(50),
    hn_tfu_new_malignancy character varying(50),
    hn_tfu_malignancy_type character varying(50),
    hn_tfu_malignancy_type_icd_o_3 character varying(50),
    hn_tfu_malignancy_date date,
    hn_tfu_local_recurrence character varying(50),
    hn_tfu_local_recurrence_date date,
    hn_tfu_regional_recurrence character varying(50),
    hn_tfu_regional_recurrence_date date,
    hn_tfu_distant_metastases character varying(50),
    hn_tfu_distant_metastases_date date
);


ALTER TABLE public.hn_tfu OWNER TO postgres;

--
-- Name: hn_tox; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hn_tox (
    hn_tox_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    hn_tox_timepoint character varying(50),
    hn_tox_date_consult date,
    hn_tox_weight real,
    hn_tox_dose_so_far real,
    hn_tox_xerostomia character varying(50),
    hn_tox_dysph character varying(50),
    hn_tox_dysph_umcg character varying(50),
    hn_tox_mucositis character varying(50),
    hn_tox_mucosa_rtog character varying(50),
    hn_tox_dermatitis character varying(50),
    hn_tox_osteoradion character varying(50),
    hn_tox_softtnecr character varying(50)
);


ALTER TABLE public.hn_tox OWNER TO postgres;

--
-- Name: ln_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ln_data (
    ln_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    ln_timepoint character varying(50),
    ln_data_entry_dt date,
    ln_bf_who character varying(150),
    ln_bf_weightloss integer,
    ln_bf_tum_loc character varying(150),
    ln_bf_central_peripheral character varying(150),
    ln_bf_histology character varying(150),
    ln_bf_ctstage character varying(150),
    ln_bf_cnstage character varying(150),
    ln_bf_cmstage character varying(150),
    ln_bf_uiccstage character varying(150),
    ln_dpr_ct_thorax character varying(150),
    ln_dpr_ct_thorax_dt date,
    ln_dpr_pet_petct character varying(150),
    ln_dpr_pet_petct_dt date,
    ln_dpr_bronchoscopy character varying(150),
    ln_dpr_mediastinoscopy character varying(150),
    ln_dpr_eus_ebus character varying(150),
    ln_dpr_lung_fn_test character varying(150),
    ln_dpr_lung_fn_fev1 integer,
    ln_dpr_lung_fn_dlco character varying(150),
    ln_pr_pri_tum_resected character varying(150),
    ln_pr_final_histology character varying(150),
    ln_pr_final_grade_diffr character varying(150),
    ln_pr_yptstage character varying(150),
    ln_pr_ypnstage character varying(150),
    ln_pr_ypmstage character varying(150),
    ln_pr_complete_resection character varying(150),
    ln_ot_chemo_seq character varying(150),
    ln_ot_chemo_completed character varying(150),
    ln_ot_immunotherapy_seq character varying(150),
    ln_rrf_rtp_ptv character varying(150),
    ln_rrf_rtp_vl character varying(150),
    ln_rrf_ptv_margin character varying(150),
    ln_rrf_mre character varying(150),
    ln_rrf_mre_translation_value character varying(150),
    ln_rrf_mre_range_uncertainity character varying(150),
    ln_rrf_mre_rotation character varying(150),
    ln_rrf_imaging_type character varying(150),
    ln_rrf_pos_correction_type character varying(150),
    ln_rrf_isocenters_nr character varying(150),
    ln_rrf_dose_engine character varying(150),
    ln_rrf_mc_uncertainity character varying(150),
    ln_rrf_treatment_tech character varying(150),
    ln_rrf_rt_photons character varying(150),
    ln_rrf_rt_protons character varying(150),
    ln_rrf_repainting_type character varying(150),
    ln_rrf_repainting_nr character varying(150),
    ln_rrf_beam_absorb_type character varying(150),
    ln_rrf_planning_pet_petct character varying(150),
    ln_rrf_4dct character varying(150),
    ln_rrf_motion_mang_tech character varying(150),
    ln_rrf_plan_adapt_strategy character varying(150),
    ln_rrf_emp_ctv_margin character varying(150),
    ln_rrf_itv character varying(150),
    ln_rrf_total_dose_prescribed character varying(150),
    ln_rrf_total_dose_actual character varying(150),
    ln_rrf_fraction_dose_planned character varying(150),
    ln_rrf_nr_fractions_planned character varying(150),
    ln_rrf_gtv_tum_vol character varying(150),
    ln_rrf_gtv_nodes_vol character varying(150),
    ln_rrf_itv_tum_vol character varying(150),
    ln_rrf_itv_nodes_vol character varying(150),
    ln_rrf_ctv_tum_vol character varying(150),
    ln_rrf_ctv_nodes_vol character varying(150),
    ln_rrf_ctv_total character varying(150),
    ln_rrf_ptv_vol character varying(150),
    ln_rrf_prt_ctv_d98 character varying(150),
    ln_rrf_prt_d2 character varying(150),
    ln_rrf_prt_dose_oars character varying(150),
    ln_rrf_pht_ptv_d98 character varying(150),
    ln_rrf_pht_ctv_d98 character varying(150),
    ln_rrf_pht_d2 character varying(150),
    ln_rrf_pht_dose_oars character varying(150),
    ln_rrf_rt_start_dt character varying(150),
    ln_rrf_rt_last_dt character varying(150),
    ln_rrf_plan1_name character varying(150),
    ln_rrf_plan1_total_dose character varying(150),
    ln_rrf_plan1_fractions character varying(150),
    ln_rrf_plan1_tech character varying(150),
    ln_rrf_plan2_name character varying(150),
    ln_rrf_plan2_total_dose character varying(150),
    ln_rrf_plan2_fractions character varying(150),
    ln_rrf_plan2_tech character varying(150),
    ln_rrf_plan3_name character varying(150),
    ln_rrf_plan3_total_dose character varying(150),
    ln_rrf_plan3_fractions character varying(150),
    ln_rrf_plan3_tech character varying(150),
    ln_rrf_plan4_name character varying(150),
    ln_rrf_plan4_total_dose character varying(150),
    ln_rrf_plan4_fractions character varying(150),
    ln_rrf_plan4_tech character varying(150),
    ln_rrf_plan5_name character varying(150),
    ln_rrf_plan5_total_dose character varying(150),
    ln_rrf_plan5_fractions character varying(150),
    ln_rrf_plan5_tech character varying(150),
    ln_rise_dysphagia character varying(150),
    ln_rise_weight integer,
    ln_rise_dermatitis_radiation character varying(150),
    ln_rise_dyspnoea character varying(150),
    ln_rise_pneumonitis character varying(150),
    ln_rise_pneumonitis_dt date,
    ln_rise_myocardial_infarction character varying(150),
    ln_rise_myocardial_infarction_dt date,
    ln_rise_heart_failure character varying(150),
    ln_rise_heart_failure_dt date,
    ln_rise_claudication_intermittens character varying(150),
    ln_rise_aortic_aneurysm character varying(150),
    ln_rise_cva character varying(150),
    ln_rise_tia character varying(150),
    ln_rise_diabetes_mellitus character varying(150),
    ln_rise_diabetes_mellitus_status character varying(150),
    ln_rise_dementia character varying(150),
    ln_rise_copd character varying(150),
    ln_rise_ctd character varying(150),
    ln_rise_pud character varying(150),
    ln_rise_liver character varying(150),
    ln_rise_hemiplegia character varying(150),
    ln_rise_ckd character varying(150),
    ln_rise_prev_solid_tum character varying(150),
    ln_rise_prev_leukaemia character varying(150),
    ln_rise_prev_lymphoma character varying(150)
);


ALTER TABLE public.ln_data OWNER TO postgres;

--
-- Name: ly_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ly_data (
    ly_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    ly_timepoint character varying(50),
    ly_data_entry_dt date,
    ly_bf_who character varying(150),
    ly_bf_weight_loss integer,
    ly_bf_nodal_sites character varying(100),
    ly_bf_nodal_lat character varying(50),
    ly_bf_exnodal_sites character varying(50),
    ly_bf_exnodal_lat character varying(50),
    ly_bf_arbor1 character varying(50),
    ly_bf_arbor2 character varying(50),
    ly_bf_bulky character varying(50),
    ly_bf_b_symp character varying(50),
    ly_bf_inv_lymph_nodes character varying(50),
    ly_bf_histology character varying(50),
    ly_bf_eortc_risk character varying(50),
    ly_bf_ghsg_risk character varying(50),
    ly_bf_ips_score character varying(50),
    ly_dpr_pre_chemo_diag character varying(50),
    ly_dpr_diag_rt_treat_pre character varying(50),
    ly_dpr_int_diag character varying(50),
    ly_dpr_deauv_score_int_scan character varying(50),
    ly_dpr_post_chemo_diag character varying(50),
    ly_dpr_diag_rt_treat_post character varying(50),
    ly_dpr_deauv_score_after_chemo character varying(50),
    ly_rise_date_consult date,
    ly_rise_dysph character varying(100),
    ly_rise_dyspn character varying(100),
    ly_rise_derm_radiat character varying(150),
    ly_rise_radiat_pneum character varying(150),
    ly_rise_brach_plex character varying(100),
    ly_rise_myoc_inf character varying(50),
    ly_rise_myoc_inf_date date,
    ly_rise_heart_fail character varying(50),
    ly_rise_heart_fail_date date,
    ly_rise_claud_interm character varying(50),
    ly_rise_aort_aneur character varying(50),
    ly_rise_cva character varying(50),
    ly_rise_tia character varying(50),
    ly_rise_diab_mel character varying(50),
    ly_rise_status_diab_mel character varying(100),
    ly_rise_dement character varying(50),
    ly_rise_copd character varying(50),
    ly_rise_con_tis_dis character varying(50),
    ly_rise_pep_ulc_dis character varying(50),
    ly_rise_liver_dis character varying(200),
    ly_rise_hemip character varying(50),
    ly_rise_chron_kid_dis character varying(150),
    ly_rise_prev_solid_tum character varying(50),
    ly_rise_prev_leuka character varying(50),
    ly_rise_prev_lymph character varying(50)
);


ALTER TABLE public.ly_data OWNER TO postgres;

--
-- Name: neu_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.neu_data (
    neu_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    neu_timepoint character varying(50),
    neu_data_entry_dt date,
    neu_gen_who character varying(150),
    neu_gen_steroids character varying(50),
    neu_gen_anti_epileptic_med character varying(50),
    neu_gen_psychiatric character varying(50),
    neu_gen_second_tumor character varying(50),
    neu_gen_second_tumor_diag_dt date,
    neu_gen_mi character varying(50),
    neu_gen_heart_fail character varying(50),
    neu_gen_pvd character varying(50),
    neu_gen_cva character varying(50),
    neu_gen_tia character varying(50),
    neu_gen_dementia character varying(50),
    neu_gen_copd character varying(50),
    neu_gen_ctd character varying(50),
    neu_gen_pud character varying(50),
    neu_gen_liver character varying(150),
    neu_gen_dm character varying(50),
    neu_gen_dm_status character varying(150),
    neu_gen_hemiplegia character varying(50),
    neu_gen_ckd character varying(150),
    neu_gen_prev_solid_tumor character varying(150),
    neu_gen_prev_leukaemia character varying(50),
    neu_gen_prev_lymphoma character varying(50),
    neu_btf_diagnosis_dt date,
    neu_btf_hist_confirmation character varying(50),
    neu_btf_hist_type character varying(150),
    neu_btf_hist_glioma_idh character varying(150),
    neu_btf_hist_glioma_codeletion character varying(150),
    neu_btf_differentiation character varying(150),
    neu_btf_laterality character varying(150),
    neu_btf_focality character varying(150),
    neu_btf_primary_lesion_loc character varying(150),
    neu_otm_tumor_surgery_dt date,
    neu_otm_extent_resection character varying(150),
    neu_otm_tumor_surgery_nr character varying(150),
    neu_otm_systemic_treatment_rt_comb character varying(50),
    neu_otm_systemic_treatment_type character varying(150),
    neu_otm_sequencing character varying(150),
    neu_otm_systemic_treatment_cources_nr integer,
    neu_rise_alopecia character varying(150),
    neu_rise_epilepsy_score character varying(150),
    neu_rise_headache character varying(150),
    neu_rise_gait_impairment character varying(150),
    neu_rise_dysphagia character varying(150),
    neu_rise_necrosis character varying(150),
    neu_rise_cognitive_disturbance character varying(150),
    neu_rise_concentration_impairment character varying(150),
    neu_rise_memory_impairment character varying(150),
    neu_rise_endocrine_problems character varying(50),
    neu_rise_endocrine_replace_therapy character varying(50),
    neu_rise_dry_eye_left character varying(150),
    neu_rise_dry_eye_right character varying(150),
    neu_rise_eye_pain_left character varying(150),
    neu_rise_eye_pain_right character varying(150),
    neu_rise_oculomotor_fn_impairment character varying(50),
    neu_rise_visual_problems character varying(50),
    neu_rise_tinnitus_left_ear character varying(150),
    neu_rise_tinnitus_right_ear character varying(150),
    neu_rise_vertigo_left_ear character varying(150),
    neu_rise_vertigo_right_ear character varying(150),
    neu_rise_hearing_impaired_left character varying(150),
    neu_rise_hearing_impaired_right character varying(150),
    neu_rise_vestibular_disorder_left_ear character varying(150),
    neu_rise_vestibular_disorder_right_ear character varying(150),
    neu_rfp_imaging_changes character varying(50),
    neu_rfp_imaging_changes_enhan character varying(50),
    neu_rfp_imaging_changes_wmh character varying(50)
);


ALTER TABLE public.neu_data OWNER TO postgres;

--
-- Name: ntcp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ntcp (
    ntcp_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    ntcp_modelversion character varying(50),
    ntcp_toxicity character varying(50),
    ntcp_grade character varying(50),
    ntcp_probability character varying(50)
);


ALTER TABLE public.ntcp OWNER TO postgres;

--
-- Name: oes_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oes_data (
    oes_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    oes_timepoint character varying(50),
    oes_data_entry_dt date,
    oes_btf_who character varying(150),
    oes_btf_weightloss integer,
    oes_btf_tumorloc character varying(150),
    oes_btf_tumorlen character varying(150),
    oes_btf_histology character varying(150),
    oes_btf_grade character varying(150),
    oes_btf_tnm_edition character varying(150),
    oes_btf_tstage character varying(150),
    oes_btf_nstage character varying(150),
    oes_btf_mstage character varying(150),
    oes_dpr_endoscopy character varying(150),
    oes_dpr_ultrasound character varying(150),
    oes_dpr_ct character varying(150),
    oes_dpr_pet character varying(150),
    oes_dpr_bronchoscopy character varying(150),
    oes_pr_histology_dt date,
    oes_pr_resec_final_histology character varying(150),
    oes_pr_resec_grade character varying(150),
    oes_pr_ypt character varying(150),
    oes_pr_ypn character varying(150),
    oes_pr_ypm character varying(150),
    oes_pr_resec_lymph_nodes_nr character varying(150),
    oes_pr_positive_lymph_nodes_nr character varying(150),
    oes_pr_resec_radicality character varying(150),
    oes_pr_tumorresponse character varying(150),
    oes_om_chemo_seq character varying(150),
    oes_om_chemo_type character varying(150),
    oes_om_chemo_completed character varying(150),
    oes_om_surgery character varying(150),
    oes_om_surgery_dt date,
    oes_rise_dysphagia character varying(150),
    oes_rise_tubefeeding character varying(150),
    oes_rise_oralmedicalnutrition character varying(150),
    oes_rise_weight character varying(150),
    oes_rise_dermatitis character varying(150),
    oes_rise_prom_oralmedicalnutrition character varying(150),
    oes_rise_esophagealperforation character varying(150),
    oes_rise_esophagealperforation_dt date,
    oes_rise_esophagealfistula character varying(150),
    oes_rise_esophagealfistula_dt date,
    oes_rise_pneumonitis character varying(150),
    oes_rise_pneumonitis_dt date,
    oes_rise_pneumonitis_rt character varying(150),
    oes_rise_myocardialinfarction character varying(150),
    oes_rise_myocardialinfarction_dt date,
    oes_rise_heartfailure character varying(150),
    oes_rise_heartfailure_dt date,
    oes_rise_claudicationintermittens character varying(150),
    oes_rise_aorticaneurysm character varying(150),
    oes_rise_cva character varying(150),
    oes_rise_tia character varying(150),
    oes_rise_diabetesmellitus character varying(150),
    oes_rise_diabetesmellitus_status character varying(150),
    oes_rise_dementia character varying(150),
    oes_rise_copd character varying(150),
    oes_rise_ctd character varying(150),
    oes_rise_pud character varying(150),
    oes_rise_liverdisease character varying(150),
    oes_rise_hemiplegia character varying(150),
    oes_rise_ckd character varying(150),
    oes_rise_solidtumor character varying(150),
    oes_rise_leukaemia character varying(150),
    oes_rise_lymphoma character varying(150)
);


ALTER TABLE public.oes_data OWNER TO postgres;

--
-- Name: to_remove_conditioncount; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.to_remove_conditioncount (
    disease character varying,
    count bigint
);


ALTER TABLE public.to_remove_conditioncount OWNER TO postgres;

--
-- Name: to_remove_consulten; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.to_remove_consulten (
    "Patientnr" character varying,
    "Vragenlijst" character varying,
    "Vraagstelling" character varying,
    "Antwoord" character varying,
    "Beantwoordingsdatum" date
);


ALTER TABLE public.to_remove_consulten OWNER TO postgres;

--
-- Name: to_remove_masterpatientindex; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.to_remove_masterpatientindex (
    patis character varying(100),
    researchnr character varying(100)
);


ALTER TABLE public.to_remove_masterpatientindex OWNER TO postgres;

--
-- Name: tumor_follow_up; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tumor_follow_up (
    tfu_id character varying(50) NOT NULL,
    gen_idnumber character varying(50) NOT NULL,
    tfu_tumorsite character varying(50) NOT NULL,
    tfu_timepoint character varying(50),
    tfu_date date,
    tfu_status character varying(50),
    tfu_new_malignancy character varying(50),
    tfu_malignancy_type character varying(50),
    tfu_malignancy_type_icd_o_3 character varying(50),
    tfu_malignancy_date date,
    tfu_local_recurrence character varying(50),
    tfu_local_recurrence_date date,
    tfu_regional_recurrence character varying(50),
    tfu_regional_recurrence_date date,
    tfu_distant_metastases character varying(50),
    tfu_distant_metastases_date date,
    tfu_location character varying(50),
    "tfu_in_or_out_RT" character varying(50)
);


ALTER TABLE public.tumor_follow_up OWNER TO postgres;

--
-- Name: eortc_br23 br23_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eortc_br23
    ADD CONSTRAINT br23_id_pkey PRIMARY KEY (br23_id);


--
-- Name: br_data br_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.br_data
    ADD CONSTRAINT br_id_pkey PRIMARY KEY (br_id);


--
-- Name: eortc_bn20 eortc_bn20_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eortc_bn20
    ADD CONSTRAINT eortc_bn20_id_pkey PRIMARY KEY (eortc_bn20_id);


--
-- Name: eortc_c30 eortc_c30_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eortc_c30
    ADD CONSTRAINT eortc_c30_id_pkey PRIMARY KEY (eortc_c30_id);


--
-- Name: eortc_hn35 eortc_hn35_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eortc_hn35
    ADD CONSTRAINT eortc_hn35_id_pkey PRIMARY KEY (eortc_hn35_id);


--
-- Name: eq_5d eq_5d_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eq_5d
    ADD CONSTRAINT eq_5d_id_pkey PRIMARY KEY (eq_5d_id);


--
-- Name: gen_alcohol gen_alcohol_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gen_alcohol
    ADD CONSTRAINT gen_alcohol_id_pkey PRIMARY KEY (gen_alcohol_id);


--
-- Name: gen_patient gen_idnumber_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gen_patient
    ADD CONSTRAINT gen_idnumber_pkey PRIMARY KEY (gen_idnumber);


--
-- Name: gen_other_cancer gen_other_cancer_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gen_other_cancer
    ADD CONSTRAINT gen_other_cancer_id_pkey PRIMARY KEY (gen_other_cancer_id);


--
-- Name: gen_plan_comparison gen_plan_comparison_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gen_plan_comparison
    ADD CONSTRAINT gen_plan_comparison_id_pkey PRIMARY KEY (gen_plan_comparison_id);


--
-- Name: gen_smoking gen_smoking_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gen_smoking
    ADD CONSTRAINT gen_smoking_id_pkey PRIMARY KEY (gen_smoking_id);


--
-- Name: hn_bl hn_bl_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hn_bl
    ADD CONSTRAINT hn_bl_id_pkey PRIMARY KEY (hn_bl_id);


--
-- Name: hn_data hn_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hn_data
    ADD CONSTRAINT hn_id_pkey PRIMARY KEY (hn_id);


--
-- Name: hn_ld hn_ld_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hn_ld
    ADD CONSTRAINT hn_ld_id_pkey PRIMARY KEY (hn_ld_id);


--
-- Name: hn_tfu hn_tfu_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hn_tfu
    ADD CONSTRAINT hn_tfu_id_pkey PRIMARY KEY (hn_tfu_id);


--
-- Name: hn_tox hn_tox_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hn_tox
    ADD CONSTRAINT hn_tox_id_pkey PRIMARY KEY (hn_tox_id);


--
-- Name: ln_data ln_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ln_data
    ADD CONSTRAINT ln_id_pkey PRIMARY KEY (ln_id);


--
-- Name: ly_data ly_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ly_data
    ADD CONSTRAINT ly_id_pkey PRIMARY KEY (ly_id);


--
-- Name: neu_data neu_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.neu_data
    ADD CONSTRAINT neu_id_pkey PRIMARY KEY (neu_id);


--
-- Name: ntcp ntcp_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ntcp
    ADD CONSTRAINT ntcp_id_pkey PRIMARY KEY (ntcp_id);


--
-- Name: oes_data oes_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oes_data
    ADD CONSTRAINT oes_id_pkey PRIMARY KEY (oes_id);


--
-- Name: tumor_follow_up tfu_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tumor_follow_up
    ADD CONSTRAINT tfu_id_pkey PRIMARY KEY (tfu_id);


--
-- Name: fki_br_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_br_gen_idnumber_fk ON public.br_data USING btree (gen_idnumber);


--
-- Name: fki_eortc_bn20_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_eortc_bn20_gen_idnumber_fk ON public.eortc_bn20 USING btree (gen_idnumber);


--
-- Name: fki_eortc_br23_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_eortc_br23_gen_idnumber_fk ON public.eortc_br23 USING btree (gen_idnumber);


--
-- Name: fki_eortc_c30_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_eortc_c30_gen_idnumber_fk ON public.eortc_c30 USING btree (gen_idnumber);


--
-- Name: fki_eortc_hn35_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_eortc_hn35_gen_idnumber_fk ON public.eortc_hn35 USING btree (gen_idnumber);


--
-- Name: fki_eq_5d_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_eq_5d_gen_idnumber_fk ON public.eq_5d USING btree (gen_idnumber);


--
-- Name: fki_gen_alcohol_patient_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_gen_alcohol_patient_fk ON public.gen_alcohol USING btree (gen_idnumber);


--
-- Name: fki_gen_plan_comparison_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_gen_plan_comparison_idnumber_fk ON public.gen_plan_comparison USING btree (gen_idnumber);


--
-- Name: fki_gen_smoking_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_gen_smoking_gen_idnumber_fk ON public.gen_smoking USING btree (gen_idnumber);


--
-- Name: fki_hn_bl_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_hn_bl_gen_idnumber_fk ON public.hn_bl USING btree (gen_idnumber);


--
-- Name: fki_hn_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_hn_gen_idnumber_fk ON public.hn_data USING btree (gen_idnumber);


--
-- Name: fki_hn_ld_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_hn_ld_gen_idnumber_fk ON public.hn_ld USING btree (gen_idnumber);


--
-- Name: fki_hn_tfu_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_hn_tfu_gen_idnumber_fk ON public.hn_tfu USING btree (gen_idnumber);


--
-- Name: fki_hn_tox_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_hn_tox_gen_idnumber_fk ON public.hn_tox USING btree (gen_idnumber);


--
-- Name: fki_ln_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_ln_gen_idnumber_fk ON public.ln_data USING btree (gen_idnumber);


--
-- Name: fki_ly_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_ly_gen_idnumber_fk ON public.ly_data USING btree (gen_idnumber);


--
-- Name: fki_neu_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_neu_gen_idnumber_fk ON public.neu_data USING btree (gen_idnumber);


--
-- Name: fki_ntcp_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_ntcp_gen_idnumber_fk ON public.ntcp USING btree (gen_idnumber);


--
-- Name: fki_oes_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_oes_gen_idnumber_fk ON public.oes_data USING btree (gen_idnumber);


--
-- Name: fki_other_cancer_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_other_cancer_gen_idnumber_fk ON public.gen_other_cancer USING btree (gen_idnumber);


--
-- Name: fki_tfu_gen_idnumber_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_tfu_gen_idnumber_fk ON public.tumor_follow_up USING btree (gen_idnumber);


--
-- PostgreSQL database dump complete
--

