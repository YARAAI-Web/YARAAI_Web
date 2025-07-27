rule auto_rule_20250726233745_5047 {
  strings:
    $o0 = "dword_42A193" wide ascii nocase
    $o1 = "dword_42A173" wide ascii nocase
    $o2 = "off_4294BF" wide ascii nocase
    $o3 = "dword_42A143" wide ascii nocase
    $o4 = "dword_42A18B" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726233746_0406 {
  strings:
    $o0 = "dword_42A14B" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726233749_9173 {
  condition:
    auto_rule_20250726233745_5047 or auto_rule_20250726233746_0406
}