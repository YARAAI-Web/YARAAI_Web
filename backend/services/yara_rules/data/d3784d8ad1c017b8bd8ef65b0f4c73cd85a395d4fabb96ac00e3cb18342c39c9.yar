rule auto_rule_20250726102258_6077 {
  strings:
    $o0 = "xFFFFC4FB" wide ascii nocase
    $o1 = "idAni" wide ascii nocase
    $o2 = "x7513u" wide ascii nocase
    $o3 = "x7D59u" wide ascii nocase
  condition:
    4 of ($o*)
}