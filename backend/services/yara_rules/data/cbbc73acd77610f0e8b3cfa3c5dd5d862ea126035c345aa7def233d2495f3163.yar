rule auto_rule_20250726082108_4719 {
  strings:
    $o0 = "x792C8900" wide ascii nocase
    $o1 = "dword_43B05C" wide ascii nocase
    $o2 = "dword_43B643" wide ascii nocase
    $o3 = "dword_43B542" wide ascii nocase
    $o4 = "dword_43B726" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726082111_7178 {
  strings:
    $o0 = "dword_43B41A" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726082117_6201 {
  condition:
    auto_rule_20250726082108_4719 or auto_rule_20250726082111_7178
}