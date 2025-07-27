rule auto_rule_20250726135834_0157 {
  strings:
    $o0 = "GdipCloneBrush" wide ascii nocase
    $o1 = "off_419170" wide ascii nocase
  condition:
    all of them
}