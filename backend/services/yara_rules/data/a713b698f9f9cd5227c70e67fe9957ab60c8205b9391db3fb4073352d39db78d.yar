rule auto_rule_20250726165756_9038 {
  strings:
    $o0 = "dword_43B761" wide ascii nocase
    $o1 = "dword_43B6BD" wide ascii nocase
    $o2 = "dword_43B6A7" wide ascii nocase
    $o3 = "send" wide ascii nocase
    $o4 = "dword_43B589" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726165759_1783 {
  strings:
    $o0 = "aOoeqtw34466Bcn" wide ascii nocase
    $o1 = "dword_43B4BE" wide ascii nocase
    $o2 = "dword_43B3F2" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726165802_7260 {
  condition:
    auto_rule_20250726165756_9038 or auto_rule_20250726165759_1783
}