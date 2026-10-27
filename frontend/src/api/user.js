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
