import request from '@/utils/request'

export function getUserInfoApi() {
  return request({
    url: '/api/user/info',
    method: 'get'
  })
}

export function updateUserInfoApi(data) {
  return request({
    url: '/api/user/me',
    method: 'put',
    data
  })
}

export function updatePasswordApi(data) {
  return request({
    url: '/api/user/password',
    method: 'put',
    data
  })
}

export function getUserPageList(params) {
  return request({
    url: '/api/user/list',
    method: 'get',
    params
  })
}

export function adminCreateUserApi(data) {
  return request({
    url: '/api/user',
    method: 'post',
    data
  })
}

export function adminUpdateUserApi(userId, data) {
  return request({
    url: `/api/user/${userId}`,
    method: 'put',
    data
  })
}

export function adminDeleteUserApi(userId) {
  return request({
    url: `/api/user/${userId}`,
    method: 'delete'
  })
}
