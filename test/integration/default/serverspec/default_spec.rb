require 'spec_helper'

describe package('telegraf') do
  it { should be_installed }
end
