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

        exam.wl_av = tmp['wl_av']

        exam.hx_av = tmp['hx_av']

        exam.sw_av = tmp['sw_av']

        exam.ls_av = tmp['ls_av']

        exam.zz_av = tmp['zz_av']

        exam.dl_av = tmp['dl_av']

        db.session.commit()

        scores = Score.query.filter_by(exam_id=exam_id).all()

        for score in scores:
            db.session.delete(score)

            db.session.commit()

        for score_data in scores_data:
            score = Score(score_data['yw'], score_data['sx'], score_data['yy'], score_data['wl'], score_data['hx'],
                          score_data['sw'], score_data['ls'], score_data['zz'], score_data['dl'], score_data['sum_3'],
                          score_data['sum_5'], score_data['class_rank_3'], score_data['class_rank_5'],
                          score_data['grade_rank_3'], score_data['grade_rank_5'], exam_id, score_data['student_id'])

            db.session.add(score)

            db.session.commit()

        return 'success'

    except Exception as e:

        print e
