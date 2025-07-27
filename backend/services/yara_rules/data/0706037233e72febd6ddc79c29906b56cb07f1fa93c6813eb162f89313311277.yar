rule auto_rule_20250726215143_4595 {
  strings:
    $o0 = "dwOemId" wide ascii nocase
    $o1 = "x425BA9" wide ascii nocase
    $o2 = "x4BB3" wide ascii nocase
    $o3 = "PeekMessagePeekMessageA" wide ascii nocase
    $o4 = "x75108AAu" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726215147_0510 {
  strings:
    $o0 = "x2B27" wide ascii nocase
    $o1 = "x93Eu" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726215151_8280 {
  condition:
    auto_rule_20250726215143_4595 or auto_rule_20250726215147_0510
}