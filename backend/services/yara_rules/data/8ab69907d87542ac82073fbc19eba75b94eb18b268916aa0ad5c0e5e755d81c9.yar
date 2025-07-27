rule auto_rule_20250726202254_9968 {
  strings:
    $o0 = "x7B6AB626" wide ascii nocase
    $o1 = "dword_4295A8" wide ascii nocase
    $o2 = "xB23B8F09" wide ascii nocase
    $o3 = "xDFF1423" wide ascii nocase
    $o4 = "dword_4295DC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726202258_3943 {
  strings:
    $o0 = "word_429720" wide ascii nocase
    $o1 = "dword_42962C" wide ascii nocase
    $o2 = "off_4298F1" wide ascii nocase
    $o3 = "x4040" wide ascii nocase
    $o4 = "x2875" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726202301_9226 {
  strings:
    $o0 = "x3F0" wide ascii nocase
    $o1 = "dword_429628" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726202311_0152 {
  condition:
    (auto_rule_20250726202254_9968 and auto_rule_20250726202258_3943) or (auto_rule_20250726202254_9968 and auto_rule_20250726202301_9226) or (auto_rule_20250726202258_3943 and auto_rule_20250726202301_9226)
}