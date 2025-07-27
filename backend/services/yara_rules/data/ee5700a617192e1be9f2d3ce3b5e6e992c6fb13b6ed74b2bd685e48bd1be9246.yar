rule auto_rule_20250726215715_0427 {
  strings:
    $o0 = "uCommand" wide ascii nocase
    $o1 = "DdeFreeDataHandle" wide ascii nocase
    $o2 = "fRedraw" wide ascii nocase
    $o3 = "lpTemplate" wide ascii nocase
    $o4 = "CreateStatusWindow" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726215718_5886 {
  strings:
    $o0 = "nBufPoints" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726215722_4114 {
  condition:
    auto_rule_20250726215715_0427 or auto_rule_20250726215718_5886
}