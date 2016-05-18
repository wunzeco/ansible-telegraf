require 'spec_helper'

describe package('telegraf') do
  it { should be_installed }
end

%w(
  /etc/telegraf/telegraf.conf
  /etc/default/telegraf
  /etc/logrotate.d/telegraf
).each do |f|
  describe file(f) do
    it { should be_file }
    it { should be_owned_by 'root' }
    it { should be_mode 644 }
  end
end

describe service('telegraf') do
  it { should be_running }
end
