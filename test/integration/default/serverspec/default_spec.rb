require 'spec_helper'

describe package('telegraf') do
  it { should be_installed }
end

describe service('telegraf') do
  it { should be_running }
end
