rule auto_rule_20250726204714_7362 {
  strings:
    $o0 = "dword_4D3064" wide ascii nocase
    $o1 = "dword_4D3124" wide ascii nocase
  condition:
    all of them
}