class HomeController < ApplicationController
  protect_from_forgery except: :takepost
  def index
  end
  def about
  end
  def blog
  end
  def contact
  end
  def takepost
    redirect_to '/'
  end
end
