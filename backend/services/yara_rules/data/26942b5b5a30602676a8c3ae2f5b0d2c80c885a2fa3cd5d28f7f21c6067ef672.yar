rule auto_rule_20250726235426_0040 {
  strings:
    $o0 = "idTransaction" wide ascii nocase
    $o1 = "uPosition" wide ascii nocase
    $o2 = "lpKeyState" wide ascii nocase
    $o3 = "hRgn" wide ascii nocase
  condition:
    4 of ($o*)
}