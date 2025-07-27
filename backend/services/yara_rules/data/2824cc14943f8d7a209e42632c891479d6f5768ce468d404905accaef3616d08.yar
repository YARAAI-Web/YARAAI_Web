rule auto_rule_20250726074001_9272 {
  strings:
    $o0 = "__crtInitCritSecNoSpinCount" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "x7FFF" wide ascii nocase
    $o3 = "dword_457E40" wide ascii nocase
    $o4 = "_RoundMan" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726074004_0672 {
  strings:
    $o0 = "dword_4577AC" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726074006_1519 {
  condition:
    auto_rule_20250726074001_9272 or auto_rule_20250726074004_0672
}