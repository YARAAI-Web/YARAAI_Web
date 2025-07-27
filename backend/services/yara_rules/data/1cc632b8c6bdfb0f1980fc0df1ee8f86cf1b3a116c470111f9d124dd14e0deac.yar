rule auto_rule_20250726130731_5711 {
  strings:
    $o0 = "dword_43B8D3" wide ascii nocase
    $o1 = "getsockopt" wide ascii nocase
    $o2 = "dword_43B162" wide ascii nocase
    $o3 = "dword_43B7FB" wide ascii nocase
    $o4 = "dword_43B020" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726130735_1425 {
  strings:
    $o0 = "dword_43B4C4" wide ascii nocase
    $o1 = "aLkaqppgqrgadaz" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726130739_5310 {
  condition:
    auto_rule_20250726130731_5711 or auto_rule_20250726130735_1425
}