import request from '@/utils/request'

export function getLabPageList(params) {
  return request({
    url: '/api/lab/list',
    method: 'get',
    params
  })
}

export function getLab(labId) {
  // 学生根据 id 查看实验室
  return request({
    url: `/api/lab/${labId}`,
    method: 'get'
  })
}

export function createLabApi(data) {
  return request({
    url: '/api/lab',
    method: 'post',
    data
  })
}

export function updateLabApi(labId, data) {
  return request({
    url: `/api/lab/${labId}`,
    method: 'put',
    data
  })
}

export function deleteLabApi(labId) {
  return request({
    url: `/api/lab/${labId}`,
    method: 'delete'
  })
}
