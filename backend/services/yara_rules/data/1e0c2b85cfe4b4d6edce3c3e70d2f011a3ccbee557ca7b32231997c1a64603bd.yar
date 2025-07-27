rule auto_rule_20250726122630_8120 {
  strings:
    $o0 = "dword_43B8CF" wide ascii nocase
    $o1 = "dword_43B62D" wide ascii nocase
    $o2 = "dword_43B86D" wide ascii nocase
    $o3 = "dword_43B758" wide ascii nocase
    $o4 = "x1FABCE00" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726122633_0768 {
  strings:
    $o0 = "dword_43B42C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726122638_4889 {
  condition:
    auto_rule_20250726122630_8120 or auto_rule_20250726122633_0768
}