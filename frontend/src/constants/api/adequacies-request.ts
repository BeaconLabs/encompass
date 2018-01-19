/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

/**
 * Request shape for POST /api/adequacies/
 */
export interface PostAdequaciesRequest {
  /**
   * Method used to calculate times and distances
   */
  method: 'driving_time' | 'haversine'
  providers: {
    /**
     * An arbitrary ID that is locally unique within this request
     */
    id: number
    latitude: number
    longitude: number
  }[]
  /**
   * Service area IDs in the format "state_city_zip".
   * For example, ["ca_san_francisco_94014", "ca_san_francisco_94015"]
   */
  service_area_ids: string[]
}
