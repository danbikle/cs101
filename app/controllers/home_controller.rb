class HomeController < ApplicationController
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
