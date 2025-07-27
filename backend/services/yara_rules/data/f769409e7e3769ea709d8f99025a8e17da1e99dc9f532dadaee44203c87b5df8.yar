rule auto_rule_20250726072339_3848 {
  strings:
    $o0 = "_isctype" wide ascii nocase
    $o1 = "RtlUnwind" wide ascii nocase
    $o2 = "dword_464434" wide ascii nocase
    $o3 = "dword_464424" wide ascii nocase
    $o4 = "dword_463C14" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726072342_5085 {
  strings:
    $o0 = "_calloc_dbg" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726072345_5574 {
  condition:
    auto_rule_20250726072339_3848 or auto_rule_20250726072342_5085
}