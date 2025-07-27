rule auto_rule_20250726235131_2128 {
  strings:
    $o0 = "dword_45D268" wide ascii nocase
    $o1 = "dword_45C2DC" wide ascii nocase
    $o2 = "GetStringTypeW" wide ascii nocase
    $o3 = "off_45C924" wide ascii nocase
    $o4 = "Runtime" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726235134_6159 {
  strings:
    $o0 = "byte_45CC14" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726235138_2662 {
  condition:
    auto_rule_20250726235131_2128 or auto_rule_20250726235134_6159
}