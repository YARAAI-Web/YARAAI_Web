rule auto_rule_20250727032054_0853 {
  strings:
    $o0 = "NonPagedPool" wide ascii nocase
    $o1 = "dword_781E4" wide ascii nocase
  condition:
    all of them
}