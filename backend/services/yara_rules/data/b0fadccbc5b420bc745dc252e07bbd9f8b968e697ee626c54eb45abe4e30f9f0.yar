rule auto_rule_20250727010706_1895 {
  strings:
    $o0 = "szClass" wide ascii nocase
    $o1 = "pbmi" wide ascii nocase
    $o2 = "stru_43458F" wide ascii nocase
  condition:
    3 of ($o*)
}