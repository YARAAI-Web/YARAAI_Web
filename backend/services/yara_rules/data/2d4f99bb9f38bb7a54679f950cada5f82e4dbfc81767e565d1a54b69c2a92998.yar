rule auto_rule_20250726085151_4295 {
  strings:
    $o0 = "old_esp" wide ascii nocase
    $o1 = "fill_with_EOS_dwords" wide ascii nocase
    $o2 = "InitializeCriticalSec" wide ascii nocase
    $o3 = "off_45C58C" wide ascii nocase
    $o4 = "x423D05" wide ascii nocase
  condition:
    4 of ($o*)
}