rule auto_rule_20250727030855_6022 {
  strings:
    $o0 = "dword_8332C" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}