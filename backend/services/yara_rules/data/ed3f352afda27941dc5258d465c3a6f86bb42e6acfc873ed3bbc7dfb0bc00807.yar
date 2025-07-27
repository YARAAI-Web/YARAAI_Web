rule auto_rule_20250726233528_2077 {
  strings:
    $o0 = "dword_40A720" wide ascii nocase
    $o1 = "x417Fu" wide ascii nocase
    $o2 = "x8FBuLL" wide ascii nocase
    $o3 = "x5E0A" wide ascii nocase
    $o4 = "x2F77u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726233532_8283 {
  strings:
    $o0 = "x6963u" wide ascii nocase
    $o1 = "x40554F" wide ascii nocase
    $o2 = "dword_40FD19" wide ascii nocase
    $o3 = "dword_40A4E0" wide ascii nocase
    $o4 = "dword_40A4F0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726233535_1259 {
  strings:
    $o0 = "x44ACu" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726233545_1684 {
  condition:
    (auto_rule_20250726233528_2077 and auto_rule_20250726233532_8283) or (auto_rule_20250726233528_2077 and auto_rule_20250726233535_1259) or (auto_rule_20250726233532_8283 and auto_rule_20250726233535_1259)
}