rule auto_rule_20250726153216_1715 {
  strings:
    $o0 = "stru_42C004" wide ascii nocase
    $o1 = "x8A4" wide ascii nocase
    $o2 = "dwPipeMode" wide ascii nocase
    $o3 = "dword_42D00C" wide ascii nocase
    $o4 = "dword_429014" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726153219_1215 {
  strings:
    $o0 = "cbOverhead" wide ascii nocase
    $o1 = "nDefaultTimeOut" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726153223_3510 {
  condition:
    auto_rule_20250726153216_1715 or auto_rule_20250726153219_1215
}