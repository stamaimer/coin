from flask import jsonify, request
from app.model.exam import Exam, db
from app.model.score import Score
from . import api


@api.route('/score', methods=['POST'])
def add_score():
    try:

        tmp = request.get_json(force=True)

        exam_name = tmp['exam_name']

        exam_id = tmp['exam_id']

        scores_data = tmp['scores']

        exam = Exam.query.filter_by(id=exam_id).first()

        exam.name = exam_name

        exam.yw_av = tmp['yw_av']

        exam.sx_av = tmp['sx_av']

        exam.yy_av = tmp['yy_av']

        exam.wl_hg_av = tmp['wl_hg_av']

        exam.hx_hg_av = tmp['hx_hg_av']

        exam.wl_dj_av = tmp['wl_dj_av']

        exam.hx_dj_av = tmp['hx_dj_av']

        exam.sw_av = tmp['sw_av']

        exam.ls_av = tmp['ls_av']

        exam.zz_av = tmp['zz_av']

        exam.dl_av = tmp['dl_av']

        exam.yw_av = tmp['yw_av']

        exam.sx_av = tmp['sx_av']

        exam.yy_stand_av = tmp['yy_stand_av']

        exam.wl_stand_av = tmp['wl_stand_av']

        exam.hx_stand_av = tmp['hx_stand_av']

        exam.sw_stand_av = tmp['sw_stand_av']

        exam.ls_stand_av = tmp['ls_stand_av']

        exam.zz_stand_av = tmp['zz_stand_av']

        exam.dl_stand_av = tmp['dl_stand_av']

        db.session.commit()

        scores = Score.query.filter_by(exam_id=exam_id).all()

        for score in scores:
            db.session.delete(score)

            db.session.commit()

        for score_data in scores_data:
            score = Score(yw=score_data['yw'], sx=score_data['sx'], yy=score_data['yy'],
                          wl_hg=score_data['wl_hg'], hx_hg=score_data['hx_hg'], wl_dj=score_data['wl_dj'],
                          hx_dj=score_data['hx_dj'], sw=score_data['sw'], ls=score_data['ls'],
                          zz=score_data['zz'], dl=score_data['dl'], sum_3=score_data['sum_3'],
                          class_rank_3=score_data['class_rank_3'], grade_rank_3=score_data['grade_rank_3'],
                          exam_id=exam_id, student_id=score_data['student_id'], yw_stand=score_data['yw_stand'],
                          sx_stand=score_data['sx_stand'], yy_stand=score_data['yy_stand'], wl_stand=score_data['wl_stand'],
                          hx_stand=score_data['hx_stand'], sw_stand=score_data['sw_stand'], ls_stand=score_data['ls_stand'],
                          zz_stand=score_data['zz_stand'], dl_stand=score_data['dl_stand'])

            db.session.add(score)

            db.session.commit()

        return 'success'

    except Exception as e:

        print e
