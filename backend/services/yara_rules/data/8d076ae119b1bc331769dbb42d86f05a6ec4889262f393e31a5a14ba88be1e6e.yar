rule auto_rule_20250726165656_7835 {
  strings:
    $o0 = "x513Fu" wide ascii nocase
    $o1 = "dword_429384" wide ascii nocase
    $o2 = "dword_429638" wide ascii nocase
    $o3 = "dword_42965C" wide ascii nocase
    $o4 = "off_429284" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726165700_6909 {
  strings:
    $o0 = "off_429A09" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726165704_4092 {
  condition:
    auto_rule_20250726165656_7835 or auto_rule_20250726165700_6909
}