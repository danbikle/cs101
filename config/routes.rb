Rails.application.routes.draw do
  get 'lessons/index'

  get  'home/index'
  root 'home#index'
  get  'home/about'
  get  'home/blog'
  get  'home/contact'
  get  '/about',   to: 'home#about'
  get  '/blog',    to: 'home#blog'
  get  '/contact', to: 'home#contact'
  get ':controller(/:action)'  
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
