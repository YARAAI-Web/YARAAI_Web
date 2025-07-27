rule auto_rule_20250726120211_7298 {
  strings:
    $o0 = "dwOptionalLength" wide ascii nocase
    $o1 = "dword_406038" wide ascii nocase
  condition:
    all of them
}