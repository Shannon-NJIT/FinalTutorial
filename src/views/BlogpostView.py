#/src/views/BlogpostView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.BlogpostModel import BlogpostModel, BlogpostSchema

blogpost_api = Blueprint('blogpost_api', __name__)
blogpost_schema = BlogpostSchema()


@blogpost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():

  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data, error = blogpost_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  post = BlogpostModel(data)
  post.save()
  data = blogpost_schema.dump(post).data
  return custom_response(data, 201)

@blogpost_api.route('/', methods=['GET'])
def get_all():
  posts = BlogpostModel.get_all_blogposts()
  data = blogpost_schema.dump(posts, many=True).data
  return custom_response(data, 200)

@blogpost_api.route('/<int:blogpost_id>', methods=['GET'])
def get_one(blogpost_id):

  post = BlogpostModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post).data
  return custom_response(data, 200)


def custom_response(res, status_code):

  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
