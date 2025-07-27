rule auto_rule_20250726063435_6596 {
  strings:
    $o0 = "dword_43B1D5" wide ascii nocase
    $o1 = "dword_43B726" wide ascii nocase
    $o2 = "aOoeqtw34466Bcn" wide ascii nocase
    $o3 = "dword_43B04C" wide ascii nocase
    $o4 = "dword_43B55A" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726063438_5559 {
  strings:
    $o0 = "dword_43B176" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726063443_3811 {
  condition:
    auto_rule_20250726063435_6596 or auto_rule_20250726063438_5559
}